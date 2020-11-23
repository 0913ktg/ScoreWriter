def notePrint(min):  # 계이름 분석 함수
    note, level = '', 0
    if min > 250 and min < 270:
        note = 'c'
        level = 3
        print('C3 - 도')
    elif min >= 271 and min <= 310:
        note = 'd'
        level = 3
        print('D3 - 레')
    elif min >= 311 and min <= 328:
        note = 'e'
        level = 3
        print('E3 - 미')
    elif min >= 329 and min <= 340:
        note = 'f'
        level = 3
        print('F3 - 파')
    elif min >= 341 and min <= 410:
        note = 'g'
        level = 3
        print('G3 - 솔')
    elif min >= 411 and min <= 465:
        note = 'a'
        level = 3
        print('A3 - 라')
    elif min >= 466 and min <= 500:
        note = 'b'
        level = 3
        print('B3 - 시')
    elif min >= 501 and min <= 560:
        note = 'c'
        level = 4
        print('C4 - 도')
    elif min >= 561 and min <= 620:
        note = 'd'
        level = 4
        print('D4 - 레')
    elif min >= 621 and min <= 675:
        note = 'e'
        level = 4
        print('E4 - 미')
    elif min >= 676 and min <= 740:
        note = 'f'
        level = 4
        print('F4 - 파')
    elif min >= 741 and min <= 840:
        note = 'g'
        level = 4
        print('G4 - 솔')

    return note, str(level+1)


def restPrint(time):
    rest = '3'
    if time >= 0.865 and time <= 1.2:
        rest = '2'
        print('2분음표')
    elif time >= 0.625 and time < 0.865:
        rest = '3'
        print('점2분음표')
    elif time >= 0.345 and time < 0.625:
        rest = '4'
        print('4분음표')
    elif time >= 0.195 and time < 0.345:
        rest = '8'
        print('8분음표')
    elif time >= 0.07 and time < 0.195:
        rest = '16'
        print('16분음표')
    return rest


def mkMeiFile(list, musicTitle):
    dur_sum = 0
    contents_top = """<?xml version="1.0" encoding="UTF-8"?>
    <?xml-model href="http://music-encoding.org/schema/3.0.0/mei-all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
    <?xml-model href="http://music-encoding.org/schema/3.0.0/mei-all.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>
    <mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="3.0.0">
        <meiHead>
            <fileDesc>
                <titleStmt>
                    <title>""" + musicTitle + """</title>
                    <respStmt>
                        <persName role="Composer">ScoreWriter</persName>
                    </respStmt>
                </titleStmt>
                <pubStmt>
                    <date>2020-06-30 10:30:00</date>
                </pubStmt>
            </fileDesc>
            <encodingDesc>
                <projectDesc>
                    <p>Transcoded from Humdrum with Verovio version 0.9.13-dev-2db4a57</p>
                    <p>Encoded by: Craig Stuart Sapp</p>
                </projectDesc>
            </encodingDesc>
            <revisionDesc>
                <change n="1">
                    <respStmt>
                        <persName>Laurent Pugin</persName>
                  </respStmt>
                    <changeDesc>
                        <p>Truncating the file and adding choice markup</p>
                    </changeDesc>
                    <date>2016-09-27</date>
                </change>
            </revisionDesc>
        </meiHead>
        <music>
            <body>
                <mdiv>
                    <score>
                        <scoreDef  midi.bpm="120">
                            <staffGrp  symbol="brace" barthru="true">
                                <staffDef  clef.shape="G" clef.line="2"  meter.count="4" meter.unit="4" n="1" lines="5" />
                            </staffGrp>
                        </scoreDef>

                        <section >
                        <measure  n="1">
                            <staff  n="1">
                                <layer  n="1">  
                                    <rest dots="1" dur="2" />
                                </layer>
                            </staff>  
                        </measure>
                            <measure  n="1">
                                <staff  n="1">
                                    <layer  n="1">
                                
                        """

    contents_bottom = """
    <rest dur="4" />
    </layer>
                                </staff>  
                            </measure>
    </section>
                    </score>
                </mdiv>
            </body>
        </music>
    </mei>


    """

    inner = ""
    for i in list:
        dur_sum += check_dur_sum(int(i['dur']))

        if(int(i['dur']) == 3):
            dur = """dots ="1" dur= """ + '"' + "2" + '"'
            note = '"' + i['note']+'"'
            oct = '"' + i['oct']+'"'

            buffer = """<chord  """ + dur + """ stem.dir="up">
                                        <note oct=""" + oct + """ pname=""" + note + """/>                                      
                                    </chord>"""

        else:
            dur = '"' + i['dur']+'"'
            note = '"' + i['note']+'"'
            oct = '"' + i['oct']+'"'

            buffer = """<chord  dur=""" + dur + """ stem.dir="up">
                                            <note oct=""" + oct + """ pname=""" + note + """/>                                      
                                        </chord>"""

        inner += buffer

        if dur_sum == 4:
            inner += """
            </layer>
                                </staff>  
                            </measure>

                            <measure  n="1">
                                <staff  n="1">
                                    <layer  n="1"> """
            dur_sum = 0

        finalresult = contents_top
        finalresult += inner
        finalresult += contents_bottom

    return finalresult


def check_dur_sum(dur):
    result = 0.0

    if dur == 1:
        result = 4
    elif dur == 2:
        result = 2
    elif dur == 3:
        result = 3
    elif dur == 4:
        result = 1
    elif dur == 8:
        result = 0.5
    elif dur == 16:
        result = 0.25
    else:
        result = 0

    return result
