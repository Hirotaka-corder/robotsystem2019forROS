# robotsystem2019forROS

# ノード間通信を行うプログラムの作成
・ノード間で数字のやり取りをチャット形式で行います

# 使用環境・言語
使用ハード：RaspberryPi 3B+

使用環境：ubuntu

使用言語：python3

# セットアップ
端末を３つ起動し、以下のようにセットアップを行います

・端末１
$roscore

・端末２
$rosrun mypkg once.py

・端末３
$rosrun mypkg twice.py

# 使い方
・上記セットアップ後に端末２、端末３にそれぞれ数字を入力することで、もう一方の端末に入力された数字が送信されます。


例１）
　端末２に
  114 
　と入力

→ 端末３に
　[INFO] [1484659840.762425]: 114
　と出力される
 
 
 例２）
 　端末３に
   514
   と入力

→ 端末２に
 　[INFO] [1484659840.762425]: 514
  と出力される


# 動画
https://www.youtube.com/watch?v=WnCHYqUvV_c&feature=youtu.be
