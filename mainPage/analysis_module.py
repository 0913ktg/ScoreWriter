note_list = [['c', '1', 32.70], ['c#', '1', 34.65], ['d', '1', 36.71], ['d#', '1', 38.89], ['e', '1', 41.20], ['f', '1', 43.65], ['f#', '1', 46.25], ['g', '1', 49.00], ['g#', '1', 51.91], ['a', '1', 55.00], ['a#', '1', 58.27], ['b', '1', 61.74],
             ['c', '2', 65], ['c#', '2', 69], ['d', '2', 73], ['d#', '2', 78], ['e', '2', 82], ['f', '2', 87], [
                 'f#', '2', 92], ['g', '2', 98], ['a', '2', 110], ['a#', '2', 117], ['b', '2', 123],
             ['c', '3', 131], ['c#', '3', 139], ['d', '3', 147], ['d#', '3', 156], ['e', '3', 165], [
                 'f', '3', 175], ['f#', '3', 185], ['g', '3', 196], ['a', '3', 220], ['a#', '3', 233], ['b', '3', 246],
             ['c', '4', 262], ['c#', '4', 277], ['d', '4', 294], ['d#', '4', 311.13], ['e', '4', 329.63], [
                 'f', '4', 349.23], ['f#', '4', 369.99], ['g', '4', 392.00], ['a', '4', 440], ['a#', '4', 466], ['b', '4', 494],
             ['c', '5', 523], ['c#', '5', 554], ['d', '5', 587], ['d#', '5', 622], ['e', '5', 659], [
                 'f', '5', 698], ['f#', '5', 740], ['g', '5', 784], ['a', '5', 880], ['a#', '5', 932], ['b', '5', 988],
             ['c', '6', 1047], ['c#', '6', 1109], ['d', '6', 1175], ['d#', '6', 1245], ['e', '6', 1319], [
                 'f', '6', 1397], ['f#', '6', 1480], ['g', '6', 1568], ['a', '6', 1760], ['a#', '6', 1865], ['b', '6', 1975],
             ['c', '7', 2093], ['c#', '7', 2217], ['d', '7', 2349], ['d#', '7', 2489], ['e', '7', 2637], [
                 'f', '7', 2794], ['f#', '7', 2960], ['g', '7', 3136], ['a', '7', 3520], ['a#', '7', 3729], ['b', '7', 3951],
             ['c', '8', 4186], ['c#', '8', 4434], ['d', '8', 4699], ['d#', '8', 4978], ['e', '8', 5274], ['f', '8', 5588], ['f#', '8', 5920], ['g', '8', 6272], ['a', '8', 7040], ['a#', '8', 7458], ['b', '8', 7902], ]


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


def notePrint2(min):
    global note_list
    if (note_list[0][2] - min) >= 0:
        min_val = note_list[0][2] - min
    else:
        min_val = 9999

    val_index = 0

    for i in range(1, len(note_list)-1):
        if (note_list[i][2] - min) < min_val and (note_list[i][2] - min) >= 0:
            print(min_val)
            min_val = note_list[i][2] - min
            val_index = i

    return note_list[val_index][0], note_list[val_index][1]


def mkMeiFile(list, musicTitle):

    dur_sum = 0
    contents_top = """<?xml version="1.0" encoding="UTF-8"?>
    <?xml-model href="http://music-encoding.org/schema/3.0.0/mei-all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
    <?xml-model href="http://music-encoding.org/schema/3.0.0/mei-all.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>
    <mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="3.0.0">
        <meiHead>
            <fileDesc>
                <titleStmt>
                    <title>"""+musicTitle+"""</title>
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
                            <measure n="1">
                                <staff n="1">
                                    <layer n="1">  
                                        <rest dur="4" />
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
