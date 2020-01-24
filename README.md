# robotsystem2019forROS

# ノード間通信を行うプログラムの作成
・ノード間で数字のやり取りをチャット形式で行います

# 使用環境・言語
使用ハード：RaspberryPi 3B+

使用環境：ubuntu

使用言語：python3

# セットアップ
端末を３つ起動し、以下のようにセットアップを行います

端末１
$roscore

$sudo insmod myledshingou.ko

$sudo mknod /dev/myled0 c [メジャー番号] [マイナー番号]

$sudo chmod 666 /dev/myled0

# 使い方
$ echo [秒数] > /dev/myled0

＊秒数は0～9の自然数


例１）
$ echo 1 > /dev/myled0 

→ GPIO23に接続されたLEDが１秒間点灯後、消灯
　その後、GPIO24に接続されたLEDが１秒間点灯後、消灯
 
 
 例２）
 $ echo 13 > /dev/myled0 

→ GPIO23に接続されたLEDが１秒間点灯後、消灯
　その後、GPIO24に接続されたLEDが１秒間点灯後、消灯
 
→ 続いて、GPIO23に接続されたLEDが３秒間点灯後、消灯
　その後、GPIO24に接続されたLEDが３秒間点灯後、消灯

# 動画
https://www.youtube.com/watch?v=WnCHYqUvV_c&feature=youtu.be

# 参考文献
https://karaage.hatenadiary.jp/entry/2018/01/19/073000

READMEの良さそうな書き方・テンプレート（最終閲覧日：2019/12/27）
