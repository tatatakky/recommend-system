# main
レコメンドシステムを作るための簡単な実装テスト。

### Description
- 今回は、与える文章を英文として実装する。
- 天気、スポーツ、コンピュータ、天気２、天気３、それぞれに関する文章を与える。
- それぞれの文章がもつ特徴を掴むために、アルゴリズムを用いて特徴ベクトルを抽出する。
- 最終的に『天気』の文章と類似度が近い文章がどの文章なのかを推定できればok。

### algorithms
- tf-idf : 特徴ベクトルの算出
- cosine-similarity : 類似度推定

### References
- https://en.wikipedia.org/wiki/Tf%E2%80%93idf</br>
- https://en.wikipedia.org/wiki/Cosine_similarity</br>
- https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/ </br>
- https://qiita.com/nmbakfm/items/6bb91b89571dd68fcea6 </br>
