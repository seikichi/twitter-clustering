##################
twcl.py
##################

What's this?
=================
Twitterのフォロー関係からユーザーをクラスタリング．
KMCの例会講座(2011/10/31)で発表したネタ(使ったデータ同梱)．

スライドは http://moon.kmc.gr.jp/~seikichi/slide/kmc111031.pdf

Run
=================
::

  % ./twcl.py < inputfile


Input file format
-----------------
::

  user1.screen_name user1.following[0].screen_name ... user1.following[n1].screen_name
  user2.screen_name user2.following[0].screen_name ... user2.following[n1].screen_name
  ...
  userM.screen_name userM.following[0].screen_name ... userM.following[n1].screen_name
  [EOF]

要するに行頭にユーザーのscreen nameを書いて, その後ろにフォローしているユーザーのscreen_nameを延々書き並べる，というのをユーザーの数だけやる．同梱の friends は seikichi/ku，seikichi/ku2，seikichi/ku3 の非protectedなユーザーから生成した例．

Requirements
-----------------
- python (>= 2.6)
- igraph_
- python-igraph_ [*]_

.. _igraph: http://cneurocvs.rmki.kfki.hu/igraph/download.html
.. _python-igraph: http://cneurocvs.rmki.kfki.hu/igraph/download.html
.. [*] python-igraph をインストールして UniqueIdGenerator で怒られる場合は igraph/clustering.py に "from datatypes import UniqueIdGenerator" を適当に追加

