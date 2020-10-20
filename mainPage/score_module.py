# Model Requires import
import librosa
import librosa.display
import librosa.core
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil

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


def add_file(input):
    global y, sr
    # file = '../Module/data/elise.mp3'
    input = '../Module/data/clock.wav'  # 추후 사용자가 업로드 한 파일을 불러올 예정
    y, sr = librosa.load(input, sr=44100)
    librosa.display.waveplot(y, sr=sr)

    create_cqt_arr()
    create_chromagram_arr()
    create_analysis_data()


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


def create_analysis_data():
    global freq, times, mags, mags_db, amin, n_fft
    freq, times, mags = librosa.core.reassigned_spectrogram(y, sr=sr)
    mags_db = librosa.power_to_db(mags**2, amin=amin, ref=np.max)

    # freq Data
    np.savetxt('../Module/data/array_Freq_all.txt',
               freq, fmt='%.3f', delimiter=", ")

    file_path = '../Module/data/array_Freq/'

    try:
        if not(os.path.isdir(file_path)):
            os.makedirs(os.path.join(file_path))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    for i in range(len(freq)):
        fname = file_path+"array_Freq_index"+str(i)+".txt"
    #     print("Make File: ", fname)
        np.savetxt(fname, freq[i], fmt='%.3f', delimiter=', ')
        for k in range(len(freq)):
            pass
    #         print(i, k, freq[i][k])

    print('array_Freq_index 정보를 저장했습니다.', '파일경로: ', file_path)

    # times Data
    np.savetxt('../Module/data/array_Times_all.txt',
               times, fmt='%.3f', delimiter=", ")

    file_path = '../Module/data/array_Times/'

    try:
        if not(os.path.isdir(file_path)):
            os.makedirs(os.path.join(file_path))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    for i in range(len(times)):
        fname = file_path+"array_Times_index"+str(i)+".txt"
    #     print("Make File: ", fname)
        np.savetxt(fname, times[i], fmt='%.3f', delimiter=', ')
        for k in range(len(times)):
            pass
    #         print(i, k, times[i][k])

    print('array_Times_index 정보를 저장했습니다.', '파일경로: ', file_path)

    # Magnitude Data
    np.savetxt('../Module/data/array_Magnitude_all.txt',
               mags_db, fmt='%.3f', delimiter=", ")

    file_path = '../Module/data/array_Magnitude/'

    try:
        if not(os.path.isdir(file_path)):
            os.makedirs(os.path.join(file_path))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    for i in range(len(mags_db)):
        fname = file_path+"array_Magnitude_index"+str(i)+".txt"
    #     print("Make File: ", fname)
        np.savetxt(fname, mags_db[i], fmt='%.3f', delimiter=', ')
        for k in range(len(mags_db)):
            pass
    #         print(i, k, mags_db[i][k])

    print('array_Magnitude_index 정보를 저장했습니다.', '파일경로: ', file_path)
