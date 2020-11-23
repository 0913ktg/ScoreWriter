# Model Requires import
import librosa
import librosa.display
import librosa.core
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
from .analysis_module import *

# 학습 시간 계산 (한국 시간으로 출력하기)
from datetime import datetime
from pytz import timezone

start_time = datetime.now(timezone('Asia/Seoul'))
end_time = ''
print('시작 시간: str', start_time)

# 분석한 자료를 초기화 하는 메서드


def clearData():
    # clear Data
    array_Chromagram_dir = '../Module/data/array_Chromagram/'
    array_CQT_dir = '../Module/data/array_CQT/'
    array_Freq_dir = '../Module/data/array_Freq/'
    array_Magnitude_dir = '../Module/data/array_Magnitude/'
    array_Times_dir = '../Module/data/array_Times/'

    directory = [
        array_Chromagram_dir,
        array_CQT_dir,
        array_Freq_dir,
        array_Magnitude_dir,
        array_Times_dir
    ]

    dir_exist = [
        os.path.isdir(array_Chromagram_dir),
        os.path.isdir(array_CQT_dir),
        os.path.isdir(array_Freq_dir),
        os.path.isdir(array_Magnitude_dir),
        os.path.isdir(array_Times_dir)
    ]
    print("디렉토리데이터 확인 ", dir_exist)

    for i, j in zip(dir_exist, directory):
        if i == True:
            print("기존데이터를 삭제합니다 폴더명: ", j)
            shutil.rmtree(j)

    array_Chromagram = '../Module/data/array_Chromagram_all.txt'
    array_CQT = '../Module/data/array_CQT_all.txt'
    array_Freq = '../Module/data/array_Freq_all.txt'
    array_Magnitude = '../Module/data/array_Magnitude_all.txt'
    array_Times = '../Module/data/array_Times_all.txt'
    freq_data = '../Module/data/freq.txt'
    mei_file = '../Module/complete_music.mei'

    file_ = [
        array_Chromagram,
        array_CQT,
        array_Freq,
        array_Magnitude,
        array_Times,
        freq_data,
        mei_file
    ]

    file_exist = [
        os.path.isfile(array_Chromagram),
        os.path.isfile(array_CQT),
        os.path.isfile(array_Freq),
        os.path.isfile(array_Magnitude),
        os.path.isfile(array_Times),
        os.path.isfile(freq_data),
        os.path.isfile(mei_file)
    ]

    print("파일데이터 확인 ", file_exist)

    for i, j in zip(file_exist, file_):
        if i == True:
            print("기존데이터를 삭제합니다 파일명: ", j)
            os.remove(j)


# Use Val
y = ''
sr = ''
CQT = ''
C = ''
freq = ''
times = ''
mags = ''
mags_db = ''
n_fft = 64
amin = 1e-10
test_arr = []
sort_arr = []
freq_arr = []
mag_arr = []
time_arr = []
analysis_body = []
musicTitle = ''


def add_file(input):
    global y, sr, musicTitle
    print(f'분석할 파일: {input}')
    musicTitle = input.split('/')
    musicTitle = musicTitle[-1]

    # file = '../Module/data/elise.mp3'
    y, sr = librosa.load(input, sr=44100)
    librosa.display.waveplot(y, sr=sr)

    create_cqt_arr()
    create_chromagram_arr()
    create_analysis_data()
    create_analysis_body()
    # 학습 총 소요시간 계산 (한국시간으로 출력하기)
    end_time = datetime.now(timezone('Asia/Seoul'))
    print('시작 시간 : '+ str(start_time))
    print('종료 시간 : '+ str(end_time))
    print()
    print('총 학습 시간 : '+ str(end_time - start_time))


def create_cqt_arr():
    global CQT, y, sr
    CQT = librosa.amplitude_to_db(np.abs(librosa.cqt(y, sr=sr)), ref=np.max)

    np.savetxt('../Module/data/array_CQT_all.txt',
               CQT, fmt='%.4f', delimiter=', ')
    # np.savetxt('../Module/data/array_CQT_index.txt', CQT,fmt='%.4f', delimiter=', ')

    file_path = '../Module/data/array_CQT/'

    try:
        if not(os.path.isdir(file_path)):
            os.makedirs(os.path.join(file_path))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    for i in range(len(CQT)):
        fname = file_path+"array_CQT_index"+str(i)+".txt"
    #     print("Make File: ", fname)
        np.savetxt(fname, CQT[i], fmt='%.4f', delimiter=', ')
        for k in range(len(CQT)):
            pass
    #         print(i, k, CQT[i][k])

    print('array_CQT_index 정보를 저장했습니다.', '파일경로: ', file_path)


def create_chromagram_arr():
    global C, y, sr
    C = librosa.feature.chroma_cqt(y=y, sr=sr)
    # print(type(C), "\n", C)
    np.savetxt('../Module/data/array_Chromagram_all.txt',
               C, fmt='%.4f', delimiter=", ")

    file_path = '../Module/data/array_Chromagram/'

    try:
        if not(os.path.isdir(file_path)):
            os.makedirs(os.path.join(file_path))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    for i in range(len(C)):
        fname = file_path + "array_Chromagram_index" + str(i) + ".txt"
    #     print("Make File: ", fname)
        np.savetxt(fname, C[i], fmt='%.4f', delimiter=', ')
    for k in range(len(C)):
        pass
    #         print(i, k, C[i][k])
    print('array_Chromagram_index 정보를 저장했습니다.', '파일경로: ', file_path)


def create_validaiton_file(file_path, data, formating):
    try:
        if not(os.path.isdir(file_path)):
            os.makedirs(os.path.join(file_path))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    for i in range(len(data)):
        fname = file_path+formating+str(i)+".txt"
    #     print("Make File: ", fname)
        np.savetxt(fname, data[i], fmt='%.3f', delimiter=', ')
        for k in range(len(data)):
            pass
    #         print(i, k, freq[i][k])

    print(formating, ' 정보를 저장했습니다.', '파일경로: ', file_path)


def create_analysis_data():
    global freq, times, mags, mags_db, amin, n_fft
    freq, times, mags = librosa.core.reassigned_spectrogram(y, sr=sr)
    mags_db = librosa.power_to_db(mags**2, amin=amin, ref=np.max)

    # freq Data
    np.savetxt('../Module/data/array_Freq_all.txt',
               freq, fmt='%.3f', delimiter=", ")

    file_path = '../Module/data/array_Freq/'

    create_validaiton_file(file_path, freq, 'array_Freq_index')

    # times Data
    np.savetxt('../Module/data/array_Times_all.txt',
               times, fmt='%.3f', delimiter=", ")

    file_path = '../Module/data/array_Times/'

    create_validaiton_file(file_path, times, 'array_Times_index')

    # Magnitude Data
    np.savetxt('../Module/data/array_Magnitude_all.txt',
               mags_db, fmt='%.3f', delimiter=", ")

    file_path = '../Module/data/array_Magnitude/'

    create_validaiton_file(file_path, mags_db, 'array_Magnitude_index')


def create_analysis_body():
    global test_arr, times, freq, mags_db, freq_arr, mag_arr, time_arr, analysis_body, musicTitle
    test_np = []
    print(freq.size)
    j_arr = []
    freq_data = []

    out_result = open('../Module/data/freq.txt', 'w')

    for atimes, afreq, amags_db in zip(times, freq, mags_db):
        for i, j, k in zip(range(0, atimes.size, 1), range(0, afreq.size, 1), range(0, amags_db.size, 1)):
            if afreq[i] and amags_db[j] >= -13:
                #             print(str.format("%.2f"% atimes[i]), " ", afreq[j], " ", amags_db[k], file=out_result)
                #             test_arr.append()
                #             print(i, " ", j)
                test_dict = {}
                test_dict['Times'] = str.format("%5.2f" % atimes[i])
                test_dict['Freq'] = float(str.format("%6.3f" % afreq[j]))

                test_dict['Magnitude'] = str.format("%6.3f" % amags_db[k])
                test_arr.append(test_dict)
    # out_result.close()
    # print("---------\n", open('data/freq.txt').read())

    sort_arr = sorted(test_arr, key=(lambda x: x['Times']))

    for i in sort_arr:
        freq_arr.append(int(i['Freq']))
        mag_arr.append(int(abs(float(i['Magnitude']))))
        time_arr.append(float(i['Times']))

    for i in sort_arr:
        print(i, file=out_result)
    out_result.close()

    minHz = 50000
    start, end, rest = 0, 0, 0
    note, octave, dur = '', '', ''

    for i in range(0, len(freq_arr)-1):
        if start == 0:
            start = time_arr[i]
            rest = start - time_arr[i-1]
        if time_arr[i] > (time_arr[i+1] - 0.03) and time_arr[i+1] != 0:
            #print(time_arr[i],"  :  ",freq_arr[i])

            if minHz > freq_arr[i]:
                minHz = freq_arr[i]
        else:
            if minHz != 50000:
                note, octave = notePrint(minHz)
                #print("sd:",start , time_arr[i+1])
                rest = restPrint(time_arr[i+1] - start)
                score_board = {}
                score_board['note'] = note
                score_board['oct'] = octave
                score_board['dur'] = rest
                analysis_body.append(score_board)
            minHz = 50000
            start = 0
    note, octave = notePrint(minHz)

    #print("sd:",start , time_arr[i+1])
    rest = restPrint(0.866)
    score_board = {}
    score_board['note'] = note
    score_board['oct'] = octave
    score_board['dur'] = rest
    analysis_body.append(score_board)

    print(start, time_arr[i+1])

    answer = mkMeiFile(analysis_body, musicTitle)

    result = open(
        '/Users/ganghansaebyeol/Documents/Develop/Python/Capston/ScoreWriter/mainPage/static/mei/complete_musics.mei', 'w')

    print(answer, file=result)
    result.close()
