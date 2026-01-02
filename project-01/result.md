
1. Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới
```csv
release_date_parsed,id,imdb_id,popularity,budget,revenue,original_title,cast,homepage,director,tagline,keywords,overview,runtime,genres,production_companies,release_date,vote_count,vote_average,release_year,budget_adj,revenue_adj
2015-12-31,382517,tt4938374,0.773909,0,0,Open Season: Scared Silly,Garry Chalk|Kathleen Barr|Willa Townsend|Melissa Sturm|Trevor Devall,http://www.sonypictures.com/movies/openseasonscaredsilly/,David Feiss,,bear|open season|elliot|boog,"The humans and animals believe a werewolf is on the loose, and former hunter Shaw uses the opportunity to re-open the season. Boog, Elliot, and Mr. Weenie have to face their fears and find the werewolf to get the season closed permanently.",85,Animation|Comedy|Family|Adventure,Sony Pictures Animation,12/31/15,33,5.6,2015,0,0
2015-12-31,362057,tt1663655,0.372889,0,0,Martyrs,Troian Bellisario|Bailey Noble|Kate Burton|Caitlin Carmichael|Melissa Tracy,,Kevin Goetz|Michael Goetz,,child abuse|sadism|female friendship|afterlife|buried alive,A woman and her childhood friend seek out revenge on those who victimized and abused them.,86,Drama|Horror|Thriller,Blumhouse Productions|The Safran Company|Temple Hill Entertainment,12/31/15,43,5,2015,0,0
...
1960-01-01,23220,tt0053677,0.333643,0,0,The Brides of Dracula,Peter Cushing|Martita Hunt|Yvonne Monlaur|Freda Jackson|David Peel,,Terence Fisher,He Turned Innocent Beauty Into Unspeakable Horror.,dracula|hammer horror|van helsing,"A young teacher on her way to a position in Transylvania helps a young man escape the shackles his mother has put on him. In so doing she innocently unleashes the horrors of the undead once again on the populace<comma> including those at her school for ladies. Luckily for some<comma> Dr Van Helsing is already on his way.",85,Horror,Hammer Film Productions|Hotspur Film Productions Ltd.,1/1/60,19,6.6,1960,0,0
```
2. Lọc ra các bộ phim có đánh giá trung bình trên 7.5 rồi lưu ra một file mới

Tổng: 350 phim
```csv
id,imdb_id,popularity,budget,revenue,original_title,cast,homepage,director,tagline,keywords,overview,runtime,genres,production_companies,release_date,vote_count,vote_average,release_year,budget_adj,revenue_adj
286217,tt3659388,7.6674,108000000,595380321,The Martian,Matt Damon|Jessica Chastain|Kristen Wiig|Jeff Daniels|Michael PeÃ±a,http://www.foxmovies.com/movies/the-martian,Ridley Scott,Bring Him Home,based on novel|mars|nasa|isolation|botanist,"During a manned mission to Mars<comma> Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. With only meager supplies<comma> he must draw upon his ingenuity<comma> wit and spirit to subsist and find a way to signal to Earth that he is alive.",141,Drama|Adventure|Science Fiction,Twentieth Century Fox Film Corporation|Scott Free Productions|Mid Atlantic Films|International Traders|TSG Entertainment,9/30/15,4572,7.6,2015,99359956.2816192,547749654.310152
...
36540,tt0061199,0.253437,0,0,Winnie the Pooh and the Honey Tree,Sterling Holloway|Junius Matthews|Sebastian Cabot|Howard Morris|Hal Smith,,Wolfgang Reitherman,,,Christopher Robin's bear attempts to raid a beehive in a tall tree.,25,Animation|Family,,1/1/66,12,7.9,1966,0,0
```
3. Tìm ra phim nào có doanh thu cao nhất và doanh thu thấp nhất

Phim có doanh thu CAO NHẤT: [Doanh thu: $2781505847] Avatar

Phim có doanh thu THẤP NHẤT:
  [Doanh thu: $2] Mallrats
  [Doanh thu: $2] Shattered Glass

4. Tính tổng doanh thu tất cả các bộ phim
432720192875

5. Top 10 bộ phim đem về lợi nhuận cao nhất

                                            Avatar | 2544505847
                      Star Wars: The Force Awakens | 1868178225
                                           Titanic | 1645034188
                                    Jurassic World | 1363528810
                                         Furious 7 | 1316249360
                                      The Avengers | 1299557910
      Harry Potter and the Deathly Hallows: Part 2 | 1202817822
                           Avengers: Age of Ultron | 1125035767
                                            Frozen | 1124219009
                                           The Net | 1084279658


6. Đạo diễn nào có nhiều bộ phim nhất và diễn viên nào đóng nhiều phim nhất

Đạo diễn: Woody Allen (46)
Diễn viên: 72 Robert De Niro (72)

7. Thống kê số lượng phim theo các thể loại. Ví dụ có bao nhiêu phim thuộc thể loại Action, bao nhiêu thuộc thể loại Family, ….

4758 Drama
3788 Comedy
2905 Thriller
2383 Action
1711 Romance
1633 Horror
1470 Adventure
1355 Crime
1231 Family
1229 Science Fiction
 915 Fantasy
 809 Mystery
 699 Animation
 520 Documentary
 408 Music
 334 History
 270 War
 188 Foreign
 167 TV Movie
 165 Western
