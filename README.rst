skkserv-lite
============

skkserv-lite は sqlite3 形式の辞書を使用する SKK サーバです。
複数辞書の使用および、サーバコンプリーションに対応しています。


インストール
------------

setup.py を使用してインストールしてください。 ::

  # python setup.py install


使用方法
--------

まずはじめに、SKK-JISYO を skkserv-lite で使用可能な sqlite3 形式に変
換します。 ::

  $ skkserv-lite -c SKK-JISYO.L SKK-JISYO.L.sqlite
  $ skkserv-lite -c SKK-JISYO.jinmei SKK-JISYO.jinmei.sqlite


デーモンとして使用する場合
~~~~~~~~~~~~~~~~~~~~~~~~~~

skkserv-lite コマンドを -d オプションをつけて起動してください。なお、
デーモンとして使用する場合には python-daemon モジュールが必要になりま
す。 ::

  $ skkserv-lite -d SKK-JISYO.L.sqlite SKK-JISYO.jinmei.sqlite

もしもフォアグラウンドで動かしたい場合には、-d の代わりに -f オプショ
ンを使用して起動してください。 ::

  $ skkserv-lite -f SKK-JISYO.L.sqlite SKK-JISYO.jinmei.sqlite


inetd を使用する場合
~~~~~~~~~~~~~~~~~~~~

skkserv-lite コマンドをオプションなしで辞書のみ指定して起動すると、
stdin から変換リクエストを読み出し stdout に書き出す動作になります。そ
のため inetd から使用したり外部コマンドとして使用したりすることができ
ます。


コンプリーションのパフォーマンス
--------------------------------

skkserv-lite では、サーバコンプリーションに sqlite3 の GLOB 式を使用し
ています。

Python の sqlite3 モジュールは SQL 文のコンパイルに sqlite3_prepare()
関数を使用していますが、この関数で LIKE や GLOB 式を使用した場合にパ
フォーマンスが非常に悪くなることがわかっています。sqlite3 モジュールに
おける sqlite3_prepare() を sqlite3_prepare_v2() に単純に置き換えてコ
ンパイルするだけで 10 倍くらい高速になります。

ただ、コンプリーションを使う頻度がそれほど高くなければ、あまり気になら
ないかもしれません。

