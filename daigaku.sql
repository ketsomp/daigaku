-- MySQL dump 10.13  Distrib 9.4.0, for macos15.4 (arm64)
--
-- Host: localhost    Database: daigaku
-- ------------------------------------------------------
-- Server version	9.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `deck`
--

DROP TABLE IF EXISTS `deck`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deck` (
  `deck_id` int NOT NULL,
  `deck_name` char(50) NOT NULL,
  `description` char(200) DEFAULT 'Japanese Vocabulary Deck',
  `language_level` int DEFAULT NULL,
  `creator_id` int NOT NULL,
  PRIMARY KEY (`deck_id`),
  KEY `fk_deck_creator` (`creator_id`),
  CONSTRAINT `fk_deck_creator` FOREIGN KEY (`creator_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `chk_language_level` CHECK ((`language_level` between 1 and 5))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deck`
--

LOCK TABLES `deck` WRITE;
/*!40000 ALTER TABLE `deck` DISABLE KEYS */;
INSERT INTO `deck` VALUES (1,'JLPT N5','Total flashcards: 51',5,1),(2,'JLPT N4','Total flashcards: 50',4,1),(3,'JLPT N3','Total flashcards: 51',3,1),(4,'JLPT N2','Total flashcards: 50',2,1),(5,'JLPT N1','Total flashcards: 50',1,1);
/*!40000 ALTER TABLE `deck` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flashcard`
--

DROP TABLE IF EXISTS `flashcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flashcard` (
  `card_id` int NOT NULL AUTO_INCREMENT,
  `deck_id` int NOT NULL,
  `expression` varchar(100) NOT NULL,
  `expression_definition` char(200) NOT NULL,
  `japanese_sentence` varchar(100) DEFAULT NULL,
  `english_translation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`card_id`),
  KEY `fk_flashcard_deck` (`deck_id`),
  CONSTRAINT `fk_flashcard_deck` FOREIGN KEY (`deck_id`) REFERENCES `deck` (`deck_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=253 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flashcard`
--

LOCK TABLES `flashcard` WRITE;
/*!40000 ALTER TABLE `flashcard` DISABLE KEYS */;
INSERT INTO `flashcard` VALUES (1,1,'私','I, me','私は学生です。','I am a student.'),(2,1,'本','book','本を読みます。','I read a book.'),(3,1,'食べる','to eat','ご飯を食べます。','I eat rice.'),(4,1,'水','water','水を飲みます。','I drink water.'),(5,1,'学校','school','学校に行きます。','I go to school.'),(6,1,'友達','friend','友達と遊びます。','I play with friends.'),(7,1,'時間','time','時間がありません。','I don\'t have time.'),(8,1,'今日','today','今日は暑いです。','It\'s hot today.'),(9,1,'明日','tomorrow','明日会いましょう。','Let\'s meet tomorrow.'),(10,1,'昨日','yesterday','昨日映画を見ました。','I watched a movie yesterday.'),(11,1,'見る','to see, watch','テレビを見ます。','I watch TV.'),(12,1,'聞く','to listen, hear','音楽を聞きます。','I listen to music.'),(13,1,'話す','to speak','日本語を話します。','I speak Japanese.'),(14,1,'書く','to write','手紙を書きます。','I write a letter.'),(15,1,'読む','to read','新聞を読みます。','I read the newspaper.'),(16,1,'行く','to go','公園に行きます。','I go to the park.'),(17,1,'来る','to come','友達が来ます。','My friend is coming.'),(18,1,'帰る','to return home','家に帰ります。','I return home.'),(19,1,'買う','to buy','服を買います。','I buy clothes.'),(20,1,'売る','to sell','本を売ります。','I sell books.'),(21,1,'作る','to make','料理を作ります。','I make food.'),(22,1,'飲む','to drink','お茶を飲みます。','I drink tea.'),(23,1,'寝る','to sleep','早く寝ます。','I sleep early.'),(24,1,'起きる','to wake up','朝早く起きます。','I wake up early in the morning.'),(25,1,'勉強する','to study','日本語を勉強します。','I study Japanese.'),(26,1,'働く','to work','会社で働きます。','I work at a company.'),(27,1,'休む','to rest','土曜日に休みます。','I rest on Saturday.'),(28,1,'立つ','to stand','駅で立ちます。','I stand at the station.'),(29,1,'座る','to sit','椅子に座ります。','I sit on a chair.'),(30,1,'歩く','to walk','公園を歩きます。','I walk in the park.'),(31,1,'走る','to run','毎朝走ります。','I run every morning.'),(32,1,'乗る','to ride','電車に乗ります。','I ride the train.'),(33,1,'降りる','to get off','次の駅で降ります。','I get off at the next station.'),(34,1,'開ける','to open','窓を開けます。','I open the window.'),(35,1,'閉める','to close','ドアを閉めます。','I close the door.'),(36,1,'使う','to use','パソコンを使います。','I use a computer.'),(37,1,'入る','to enter','部屋に入ります。','I enter the room.'),(38,1,'出る','to exit, leave','家を出ます。','I leave home.'),(39,1,'会う','to meet','友達に会います。','I meet a friend.'),(40,1,'待つ','to wait','友達を待ちます。','I wait for a friend.'),(41,1,'持つ','to hold, have','かばんを持ちます。','I hold a bag.'),(42,1,'知る','to know','この人を知っています。','I know this person.'),(43,1,'分かる','to understand','日本語が分かります。','I understand Japanese.'),(44,1,'思う','to think','それは良いと思います。','I think that\'s good.'),(45,1,'言う','to say','何も言いません。','I say nothing.'),(46,1,'教える','to teach','英語を教えます。','I teach English.'),(47,1,'習う','to learn','ピアノを習います。','I learn piano.'),(48,1,'始める','to begin','勉強を始めます。','I begin studying.'),(49,1,'終わる','to end','授業が終わります。','Class ends.'),(50,1,'忘れる','to forget','名前を忘れました。','I forgot the name.'),(51,2,'頑張る','to do one\'s best','試験を頑張ります。','I\'ll do my best on the exam.'),(52,2,'困る','to be troubled','お金がなくて困ります。','I\'m troubled because I have no money.'),(53,2,'決める','to decide','旅行の日を決めます。','I decide the travel date.'),(54,2,'遊ぶ','to play','週末友達と遊びます。','I play with friends on weekends.'),(55,2,'笑う','to laugh','面白い話で笑います。','I laugh at funny stories.'),(56,2,'泣く','to cry','悲しい映画で泣きます。','I cry at sad movies.'),(57,2,'怒る','to get angry','彼は遅れて怒りました。','He got angry about being late.'),(58,2,'疲れる','to get tired','仕事で疲れます。','I get tired from work.'),(59,2,'選ぶ','to choose','好きな色を選びます。','I choose my favorite color.'),(60,2,'比べる','to compare','二つの商品を比べます。','I compare two products.'),(61,2,'変える','to change','予定を変えます。','I change plans.'),(62,2,'増える','to increase','人口が増えます。','The population increases.'),(63,2,'減る','to decrease','お金が減ります。','Money decreases.'),(64,2,'続ける','to continue','勉強を続けます。','I continue studying.'),(65,2,'止める','to stop','車を止めます。','I stop the car.'),(66,2,'付ける','to attach, turn on','電気を付けます。','I turn on the light.'),(67,2,'消す','to turn off, erase','電気を消します。','I turn off the light.'),(68,2,'壊れる','to break','時計が壊れました。','The watch broke.'),(69,2,'直す','to fix, correct','間違いを直します。','I correct mistakes.'),(70,2,'探す','to search for','鍵を探します。','I search for keys.'),(71,2,'見つける','to find','良い店を見つけます。','I find a good store.'),(72,2,'失う','to lose','大切なものを失いました。','I lost something important.'),(73,2,'拾う','to pick up','道で財布を拾いました。','I picked up a wallet on the street.'),(74,2,'捨てる','to throw away','ゴミを捨てます。','I throw away trash.'),(75,2,'貸す','to lend','友達に本を貸します。','I lend a book to a friend.'),(76,2,'借りる','to borrow','図書館で本を借ります。','I borrow books from the library.'),(77,2,'返す','to return','借りた本を返します。','I return borrowed books.'),(78,2,'送る','to send','メールを送ります。','I send an email.'),(79,2,'届く','to reach, arrive','荷物が届きました。','The package arrived.'),(80,2,'渡す','to hand over','プレゼントを渡します。','I hand over a present.'),(81,2,'もらう','to receive','お土産をもらいました。','I received a souvenir.'),(82,2,'あげる','to give','花をあげます。','I give flowers.'),(83,2,'くれる','to give (to me)','友達がくれました。','My friend gave it to me.'),(84,2,'助ける','to help','困っている人を助けます。','I help people in trouble.'),(85,2,'頼む','to request, ask','手伝いを頼みます。','I ask for help.'),(86,2,'誘う','to invite','パーティーに誘います。','I invite to a party.'),(87,2,'断る','to refuse','招待を断りました。','I refused the invitation.'),(88,2,'謝る','to apologize','遅れて謝ります。','I apologize for being late.'),(89,2,'褒める','to praise','良い仕事を褒めます。','I praise good work.'),(90,2,'注意する','to warn, be careful','危険に注意します。','I\'m careful of danger.'),(91,2,'確認する','to confirm','予約を確認します。','I confirm the reservation.'),(92,2,'準備する','to prepare','旅行の準備をします。','I prepare for the trip.'),(93,2,'片付ける','to tidy up','部屋を片付けます。','I tidy up the room.'),(94,2,'掃除する','to clean','毎日掃除します。','I clean every day.'),(95,2,'洗う','to wash','手を洗います。','I wash my hands.'),(96,2,'拭く','to wipe','テーブルを拭きます。','I wipe the table.'),(97,2,'磨く','to polish, brush','歯を磨きます。','I brush my teeth.'),(98,2,'混む','to be crowded','電車が混みます。','The train is crowded.'),(99,2,'空く','to become empty','席が空きました。','A seat became empty.'),(100,2,'並ぶ','to line up','レジに並びます。','I line up at the register.'),(101,3,'達成する','to achieve','目標を達成しました。','I achieved my goal.'),(102,3,'実現する','to realize','夢を実現します。','I realize my dream.'),(103,3,'成功する','to succeed','ビジネスに成功しました。','I succeeded in business.'),(104,3,'失敗する','to fail','試験に失敗しました。','I failed the exam.'),(105,3,'発展する','to develop','技術が発展します。','Technology develops.'),(106,3,'進歩する','to progress','科学が進歩します。','Science progresses.'),(107,3,'向上する','to improve','成績が向上しました。','My grades improved.'),(108,3,'低下する','to decline','品質が低下します。','Quality declines.'),(109,3,'維持する','to maintain','健康を維持します。','I maintain health.'),(110,3,'保存する','to preserve','データを保存します。','I save data.'),(111,3,'破壊する','to destroy','環境を破壊します。','Destroy the environment.'),(112,3,'創造する','to create','新しいものを創造します。','I create something new.'),(113,3,'表現する','to express','気持ちを表現します。','I express feelings.'),(114,3,'理解する','to understand','意味を理解します。','I understand the meaning.'),(115,3,'説明する','to explain','ルールを説明します。','I explain the rules.'),(116,3,'証明する','to prove','理論を証明します。','I prove the theory.'),(117,3,'判断する','to judge','正しく判断します。','I judge correctly.'),(118,3,'評価する','to evaluate','結果を評価します。','I evaluate the results.'),(119,3,'批判する','to criticize','政策を批判します。','I criticize policies.'),(120,3,'賛成する','to agree','提案に賛成します。','I agree with the proposal.'),(121,3,'反対する','to oppose','計画に反対します。','I oppose the plan.'),(122,3,'主張する','to insist','意見を主張します。','I insist on my opinion.'),(123,3,'議論する','to discuss','問題を議論します。','I discuss the problem.'),(124,3,'協力する','to cooperate','チームで協力します。','I cooperate with the team.'),(125,3,'競争する','to compete','他社と競争します。','I compete with other companies.'),(126,3,'妥協する','to compromise','両方が妥協します。','Both sides compromise.'),(127,3,'克服する','to overcome','困難を克服します。','I overcome difficulties.'),(128,3,'解決する','to solve','問題を解決します。','I solve problems.'),(129,3,'対応する','to respond','要求に対応します。','I respond to demands.'),(130,3,'適応する','to adapt','環境に適応します。','I adapt to the environment.'),(131,3,'貢献する','to contribute','社会に貢献します。','I contribute to society.'),(132,3,'参加する','to participate','会議に参加します。','I participate in meetings.'),(133,3,'出席する','to attend','授業に出席します。','I attend class.'),(134,3,'欠席する','to be absent','学校を欠席しました。','I was absent from school.'),(135,3,'延期する','to postpone','会議を延期します。','I postpone the meeting.'),(136,3,'中止する','to cancel','イベントを中止します。','I cancel the event.'),(137,3,'実施する','to implement','計画を実施します。','I implement the plan.'),(138,3,'実行する','to execute','命令を実行します。','I execute orders.'),(139,3,'承認する','to approve','申請を承認します。','I approve applications.'),(140,3,'拒否する','to reject','要求を拒否します。','I reject demands.'),(141,3,'禁止する','to prohibit','喫煙を禁止します。','I prohibit smoking.'),(142,3,'許可する','to permit','使用を許可します。','I permit usage.'),(143,3,'命令する','to order','部下に命令します。','I order subordinates.'),(144,3,'要求する','to demand','改善を要求します。','I demand improvements.'),(145,3,'依頼する','to request','仕事を依頼します。','I request work.'),(146,3,'提案する','to propose','新しい案を提案します。','I propose a new idea.'),(147,3,'推薦する','to recommend','本を推薦します。','I recommend books.'),(148,3,'紹介する','to introduce','友人を紹介します。','I introduce friends.'),(149,3,'招待する','to invite','結婚式に招待します。','I invite to a wedding.'),(150,3,'案内する','to guide','道を案内します。','I guide the way.'),(151,4,'抽象的','abstract','抽象的な概念です。','It\'s an abstract concept.'),(152,4,'具体的','concrete','具体的な例を示します。','I show concrete examples.'),(153,4,'複雑','complex','問題が複雑です。','The problem is complex.'),(154,4,'単純','simple','答えは単純です。','The answer is simple.'),(155,4,'曖昧','ambiguous','説明が曖昧です。','The explanation is ambiguous.'),(156,4,'明確','clear','意図が明確です。','The intention is clear.'),(157,4,'顕著','remarkable','変化が顕著です。','The change is remarkable.'),(158,4,'微妙','subtle','違いが微妙です。','The difference is subtle.'),(159,4,'深刻','serious','状況が深刻です。','The situation is serious.'),(160,4,'軽微','minor','被害は軽微です。','The damage is minor.'),(161,4,'重大','grave','重大な問題です。','It\'s a grave problem.'),(162,4,'些細','trivial','些細なことです。','It\'s a trivial matter.'),(163,4,'膨大','enormous','データが膨大です。','The data is enormous.'),(164,4,'僅か','slight','僅かな差です。','It\'s a slight difference.'),(165,4,'著しい','notable','進歩が著しいです。','Progress is notable.'),(166,4,'顕在化する','to become apparent','問題が顕在化しました。','The problem became apparent.'),(167,4,'潜在的','latent','潜在的な危険があります。','There\'s latent danger.'),(168,4,'根本的','fundamental','根本的な解決が必要です。','A fundamental solution is needed.'),(169,4,'表面的','superficial','理解が表面的です。','Understanding is superficial.'),(170,4,'本質的','essential','本質的な問題です。','It\'s an essential problem.'),(171,4,'一時的','temporary','一時的な措置です。','It\'s a temporary measure.'),(172,4,'永続的','permanent','永続的な平和を望みます。','I wish for permanent peace.'),(173,4,'相対的','relative','価値は相対的です。','Value is relative.'),(174,4,'絶対的','absolute','絶対的な真実です。','It\'s an absolute truth.'),(175,4,'包括的','comprehensive','包括的な調査です。','It\'s a comprehensive survey.'),(176,4,'限定的','limited','効果は限定的です。','The effect is limited.'),(177,4,'普遍的','universal','普遍的な法則です。','It\'s a universal law.'),(178,4,'特殊','special','特殊な状況です。','It\'s a special situation.'),(179,4,'一般的','general','一般的な意見です。','It\'s a general opinion.'),(180,4,'個別','individual','個別に対応します。','I respond individually.'),(181,4,'統一する','to unify','規格を統一します。','I unify standards.'),(182,4,'分割する','to divide','作業を分割します。','I divide the work.'),(183,4,'統合する','to integrate','システムを統合します。','I integrate systems.'),(184,4,'分離する','to separate','物質を分離します。','I separate substances.'),(185,4,'融合する','to fuse','文化が融合します。','Cultures fuse.'),(186,4,'独立する','to be independent','会社から独立しました。','I became independent from the company.'),(187,4,'依存する','to depend','輸入に依存します。','I depend on imports.'),(188,4,'関連する','to relate','事件に関連します。','It relates to the incident.'),(189,4,'無関係','unrelated','二つは無関係です。','The two are unrelated.'),(190,4,'直接','direct','直接話します。','I speak directly.'),(191,4,'間接的','indirect','間接的な影響です。','It\'s an indirect influence.'),(192,4,'積極的','positive','積極的に参加します。','I participate actively.'),(193,4,'消極的','passive','態度が消極的です。','The attitude is passive.'),(194,4,'能動的','active','能動的に動きます。','I act actively.'),(195,4,'受動的','passive','受動的な姿勢です。','It\'s a passive posture.'),(196,4,'自発的','voluntary','自発的に手伝います。','I help voluntarily.'),(197,4,'強制的','compulsory','強制的な措置です。','It\'s a compulsory measure.'),(198,4,'意図的','intentional','意図的な行動です。','It\'s intentional behavior.'),(199,4,'偶然','accidental','偶然の出会いです。','It\'s an accidental meeting.'),(200,4,'必然的','inevitable','結果は必然的です。','The result is inevitable.'),(201,5,'錯綜する','to be complicated','情報が錯綜しています。','Information is complicated.'),(202,5,'紛糾する','to be in a tangle','議論が紛糾しました。','The discussion got tangled.'),(203,5,'煩雑','troublesome','手続きが煩雑です。','Procedures are troublesome.'),(204,5,'繁雑','intricate','作業が繁雑です。','The work is intricate.'),(205,5,'緻密','meticulous','計画が緻密です。','The plan is meticulous.'),(206,5,'粗雑','rough','仕事が粗雑です。','The work is rough.'),(207,5,'精巧','elaborate','細工が精巧です。','The craft is elaborate.'),(208,5,'粗悪','inferior','品質が粗悪です。','Quality is inferior.'),(209,5,'卓越する','to excel','技術に卓越しています。','I excel in technology.'),(210,5,'凡庸','mediocre','能力が凡庸です。','Ability is mediocre.'),(211,5,'顕著','conspicuous','効果が顕著です。','The effect is conspicuous.'),(212,5,'希薄','thin','関係が希薄です。','The relationship is thin.'),(213,5,'濃密','dense','時間が濃密です。','Time is dense.'),(214,5,'希少','rare','資源が希少です。','Resources are rare.'),(215,5,'豊富','abundant','経験が豊富です。','Experience is abundant.'),(216,5,'欠乏する','to lack','栄養が欠乏します。','Nutrition is lacking.'),(217,5,'充足する','to be satisfied','条件が充足します。','Conditions are satisfied.'),(218,5,'飽和する','to be saturated','市場が飽和しました。','The market is saturated.'),(219,5,'枯渇する','to be exhausted','資源が枯渇します。','Resources are exhausted.'),(220,5,'蓄積する','to accumulate','知識が蓄積します。','Knowledge accumulates.'),(221,5,'消耗する','to be worn out','体力が消耗します。','Physical strength wears out.'),(222,5,'補充する','to replenish','在庫を補充します。','I replenish inventory.'),(223,5,'補完する','to complement','互いに補完します。','We complement each other.'),(224,5,'代替する','to substitute','製品を代替します。','I substitute products.'),(225,5,'模倣する','to imitate','デザインを模倣します。','I imitate designs.'),(226,5,'創出する','to create','価値を創出します。','I create value.'),(227,5,'派生する','to derive','問題が派生します。','Problems derive.'),(228,5,'誘発する','to induce','反応を誘発します。','I induce reactions.'),(229,5,'抑制する','to suppress','欲望を抑制します。','I suppress desires.'),(230,5,'促進する','to promote','成長を促進します。','I promote growth.'),(231,5,'阻害する','to hinder','進歩を阻害します。','I hinder progress.'),(232,5,'妨害する','to obstruct','計画を妨害します。','I obstruct plans.'),(233,5,'擁護する','to defend','権利を擁護します。','I defend rights.'),(234,5,'攻撃する','to attack','敵を攻撃します。','I attack enemies.'),(235,5,'防御する','to defend','国を防御します。','I defend the country.'),(236,5,'侵害する','to infringe','著作権を侵害します。','I infringe copyright.'),(237,5,'遵守する','to observe','法律を遵守します。','I observe laws.'),(238,5,'違反する','to violate','規則に違反します。','I violate rules.'),(239,5,'逸脱する','to deviate','基準から逸脱します。','I deviate from standards.'),(240,5,'遭遇する','to encounter','困難に遭遇します。','I encounter difficulties.'),(241,5,'直面する','to face','危機に直面します。','I face a crisis.'),(242,5,'回避する','to avoid','リスクを回避します。','I avoid risks.'),(243,5,'克服する','to overcome','障害を克服します。','I overcome obstacles.'),(244,5,'凌駕する','to surpass','期待を凌駕します。','I surpass expectations.'),(245,5,'匹敵する','to rival','実力が匹敵します。','Abilities rival.'),(246,5,'劣る','to be inferior','品質が劣ります。','Quality is inferior.'),(247,5,'勝る','to be superior','性能が勝ります。','Performance is superior.'),(248,5,'凌ぐ','to surpass','前作を凌ぎます。','I surpass the previous work.'),(249,5,'追随する','to follow','流行に追随します。','I follow trends.'),(250,5,'先駆ける','to pioneer','分野を先駆けます。','I pioneer the field.'),(251,1,'黄昏','twilight','黄昏は暗い。','Twilight is dark.'),(252,3,'犬','wefr','fewrg','rfegt');
/*!40000 ALTER TABLE `flashcard` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `trg_after_flashcard_insert` AFTER INSERT ON `flashcard` FOR EACH ROW BEGIN
    UPDATE deck
    SET description = CONCAT('Total flashcards: ', (
        SELECT COUNT(*) FROM flashcard WHERE deck_id = NEW.deck_id
    ))
    WHERE deck_id = NEW.deck_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `immersion_material`
--

DROP TABLE IF EXISTS `immersion_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `immersion_material` (
  `material_id` int NOT NULL,
  `title` varchar(50) NOT NULL,
  `purchase_website_url` varchar(100) DEFAULT NULL,
  `type` char(20) NOT NULL,
  `source` varchar(100) DEFAULT NULL,
  `length` int DEFAULT NULL,
  `average_difficulty` int DEFAULT NULL,
  PRIMARY KEY (`material_id`),
  CONSTRAINT `chk_avg_difficulty` CHECK ((`average_difficulty` between 1 and 5)),
  CONSTRAINT `chk_material_type` CHECK ((`type` in (_utf8mb4'television',_utf8mb4'movie',_utf8mb4'book',_utf8mb4'podcast')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `immersion_material`
--

LOCK TABLES `immersion_material` WRITE;
/*!40000 ALTER TABLE `immersion_material` DISABLE KEYS */;
INSERT INTO `immersion_material` VALUES (1,'Naruto','https://www.crunchyroll.com/naruto','television','Crunchyroll',480,3),(2,'Attack on Titan','https://www.crunchyroll.com/attack-on-titan','television','Crunchyroll',300,4),(3,'One Piece','https://www.crunchyroll.com/one-piece','television','Crunchyroll',12000,3),(4,'Death Note','https://www.netflix.com/death-note','television','Netflix',552,4),(5,'Demon Slayer','https://www.crunchyroll.com/demon-slayer','television','Crunchyroll',312,3),(6,'My Hero Academia','https://www.crunchyroll.com/my-hero-academia','television','Crunchyroll',720,3),(7,'Steins;Gate','https://www.crunchyroll.com/steinsgate','television','Crunchyroll',600,4),(8,'Fullmetal Alchemist','https://www.crunchyroll.com/fullmetal-alchemist','television','Crunchyroll',1560,4),(9,'Sword Art Online','https://www.crunchyroll.com/sword-art-online','television','Crunchyroll',1200,3),(10,'Tokyo Ghoul','https://www.crunchyroll.com/tokyo-ghoul','television','Crunchyroll',576,4),(11,'Your Name','https://www.crunchyroll.com/your-name','movie','Crunchyroll',106,3),(12,'Spirited Away','https://www.hbomax.com/spirited-away','movie','HBO Max',125,3),(13,'A Silent Voice','https://www.netflix.com/a-silent-voice','movie','Netflix',130,4),(14,'Weathering With You','https://www.crunchyroll.com/weathering-with-you','movie','Crunchyroll',114,3),(15,'Howl\'s Moving Castle','https://www.hbomax.com/howls-moving-castle','movie','HBO Max',119,3),(16,'Norwegian Wood','https://www.amazon.com/norwegian-wood','book','Amazon',NULL,4),(17,'Kitchen','https://www.amazon.com/kitchen-banana','book','Amazon',NULL,3),(18,'1Q84','https://www.amazon.com/1q84','book','Amazon',NULL,5),(19,'Battle Royale','https://www.amazon.com/battle-royale','book','Amazon',NULL,4),(20,'Kafka on the Shore','https://www.amazon.com/kafka-shore','book','Amazon',NULL,5),(21,'JapanesePod101','https://www.japanesepod101.com','podcast','JapanesePod101',30,2),(22,'NHK Easy Japanese','https://www.nhk.or.jp/lesson','podcast','NHK',20,2),(23,'Learn Japanese Pod','https://www.learnjapanesepod.com','podcast','Learn Japanese Pod',45,3),(24,'Nihongo con Teppei','https://nihongoconteppei.com','podcast','Teppei Sensei',15,3),(25,'Bilingual News','https://bilingualnews.jp','podcast','Bilingual News',60,4),(26,'anime','youtube','television','youtube',NULL,3);
/*!40000 ALTER TABLE `immersion_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_vocab_map`
--

DROP TABLE IF EXISTS `material_vocab_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material_vocab_map` (
  `material_id` int NOT NULL,
  `vocab_id` int NOT NULL,
  PRIMARY KEY (`material_id`),
  KEY `fk_material_vocab_map_vocabulary` (`vocab_id`),
  CONSTRAINT `fk_material_vocab_map_immersion` FOREIGN KEY (`material_id`) REFERENCES `immersion_material` (`material_id`),
  CONSTRAINT `fk_material_vocab_map_vocabulary` FOREIGN KEY (`vocab_id`) REFERENCES `vocabulary` (`vocabulary_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_vocab_map`
--

LOCK TABLES `material_vocab_map` WRITE;
/*!40000 ALTER TABLE `material_vocab_map` DISABLE KEYS */;
/*!40000 ALTER TABLE `material_vocab_map` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL,
  `username` char(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(20) NOT NULL,
  `date_joined` date NOT NULL DEFAULT (curdate()),
  `current_level` int DEFAULT '5',
  `vocabulary_learnt` int DEFAULT '0',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `uq_username` (`username`),
  UNIQUE KEY `uq_email` (`email`),
  CONSTRAINT `chk_current_level` CHECK ((`current_level` between 1 and 5)),
  CONSTRAINT `chk_password_length` CHECK ((length(`password_hash`) >= 8))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'root','root@daigaku.com','rootpass','2025-10-10',5,0),(2,'customer','customer@daigaku.com','customer1','2025-10-31',3,0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_card_review`
--

DROP TABLE IF EXISTS `user_card_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_card_review` (
  `review_id` int NOT NULL,
  `user_id` int NOT NULL,
  `card_id` int NOT NULL,
  `review_date` date NOT NULL,
  `answer_quality` int NOT NULL,
  `time_taken` datetime DEFAULT NULL,
  PRIMARY KEY (`review_id`),
  KEY `fk_user_card_review_user` (`user_id`),
  KEY `fk_user_card_review_flashcard` (`card_id`),
  CONSTRAINT `fk_user_card_review_flashcard` FOREIGN KEY (`card_id`) REFERENCES `flashcard` (`card_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_user_card_review_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `chk_answer_quality` CHECK ((`answer_quality` between 1 and 5))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_card_review`
--

LOCK TABLES `user_card_review` WRITE;
/*!40000 ALTER TABLE `user_card_review` DISABLE KEYS */;
INSERT INTO `user_card_review` VALUES (1,1,1,'2025-10-31',5,'2025-10-31 11:35:22'),(2,1,2,'2025-10-31',4,'2025-10-31 11:35:22'),(3,1,3,'2025-10-31',3,'2025-10-31 11:35:22'),(4,1,4,'2025-10-31',4,'2025-10-31 11:35:22'),(5,1,5,'2025-10-31',3,'2025-10-31 11:35:22'),(6,1,6,'2025-10-31',4,'2025-10-31 11:35:22'),(7,1,7,'2025-10-31',3,'2025-10-31 11:35:22'),(8,1,8,'2025-10-31',5,'2025-10-31 11:35:22'),(9,1,9,'2025-10-31',4,'2025-10-31 11:35:22'),(10,1,10,'2025-10-31',3,'2025-10-31 11:35:22'),(11,1,11,'2025-10-31',4,'2025-10-31 11:35:22'),(12,1,12,'2025-10-31',5,'2025-10-31 11:35:22'),(13,1,13,'2025-10-31',3,'2025-10-31 11:35:22'),(14,1,14,'2025-10-31',3,'2025-10-31 11:35:22'),(15,1,15,'2025-10-31',4,'2025-10-31 11:35:22'),(16,1,16,'2025-10-31',3,'2025-10-31 11:35:22'),(17,1,17,'2025-10-31',5,'2025-10-31 11:35:22'),(18,1,18,'2025-10-31',3,'2025-10-31 11:35:22'),(19,1,19,'2025-10-31',4,'2025-10-31 11:35:22'),(20,1,20,'2025-10-31',4,'2025-10-31 11:35:22'),(21,1,21,'2025-10-31',4,'2025-10-31 11:35:22'),(22,1,22,'2025-10-31',4,'2025-10-31 11:35:22'),(23,1,23,'2025-10-31',5,'2025-10-31 11:35:22'),(24,1,24,'2025-10-31',3,'2025-10-31 11:35:22'),(25,1,25,'2025-10-31',3,'2025-10-31 11:35:22'),(26,2,1,'2025-10-31',3,'2025-10-31 11:35:22'),(27,2,2,'2025-10-31',4,'2025-10-31 11:35:22'),(28,2,3,'2025-10-31',2,'2025-10-31 11:35:22'),(29,2,4,'2025-10-31',4,'2025-10-31 11:35:22'),(30,2,5,'2025-10-31',3,'2025-10-31 11:35:22'),(31,2,6,'2025-10-31',2,'2025-10-31 11:35:22'),(32,2,7,'2025-10-31',4,'2025-10-31 11:35:22'),(33,2,8,'2025-10-31',3,'2025-10-31 11:35:22'),(34,2,9,'2025-10-31',2,'2025-10-31 11:35:22'),(35,2,10,'2025-10-31',3,'2025-10-31 11:35:22'),(36,1,201,'2025-10-31',1,'2025-10-31 11:35:53'),(37,1,202,'2025-10-31',1,'2025-10-31 11:35:54'),(38,1,151,'2025-10-31',2,'2025-10-31 14:25:32'),(39,1,152,'2025-10-31',4,'2025-10-31 14:25:34'),(40,1,153,'2025-10-31',3,'2025-10-31 14:25:36'),(41,1,101,'2025-11-04',3,'2025-11-04 09:45:50'),(42,1,102,'2025-11-04',5,'2025-11-04 09:45:51'),(43,1,103,'2025-11-04',3,'2025-11-04 09:46:03'),(44,1,26,'2025-11-04',3,'2025-11-04 09:55:21'),(45,1,104,'2025-11-04',3,'2025-11-04 13:34:31'),(46,1,105,'2025-11-04',4,'2025-11-04 13:34:33'),(47,1,106,'2025-11-04',4,'2025-11-04 13:34:40'),(48,1,107,'2025-11-04',2,'2025-11-04 13:34:42'),(49,1,108,'2025-11-04',4,'2025-11-04 13:50:33'),(50,1,109,'2025-11-04',3,'2025-11-04 13:50:36');
/*!40000 ALTER TABLE `user_card_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_material_history`
--

DROP TABLE IF EXISTS `user_material_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_material_history` (
  `history_id` int NOT NULL,
  `user_id` int NOT NULL,
  `material_id` int NOT NULL,
  `saved_for_later` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `fk_user_material_history_user` (`user_id`),
  KEY `fk_user_material_history_immersion` (`material_id`),
  CONSTRAINT `fk_user_material_history_immersion` FOREIGN KEY (`material_id`) REFERENCES `immersion_material` (`material_id`),
  CONSTRAINT `fk_user_material_history_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_material_history`
--

LOCK TABLES `user_material_history` WRITE;
/*!40000 ALTER TABLE `user_material_history` DISABLE KEYS */;
INSERT INTO `user_material_history` VALUES (1,1,1,NULL),(2,1,2,NULL),(3,1,4,'Want to rewatch'),(4,1,5,NULL),(5,1,11,'Favorite movie'),(6,1,12,NULL),(7,1,18,'Reading now'),(8,1,25,NULL),(9,2,1,NULL),(10,2,5,'Currently watching'),(11,2,6,NULL),(12,2,11,'Watched 3 times'),(13,2,14,NULL),(14,2,17,'First Japanese book'),(15,2,21,'Daily listening'),(16,2,22,NULL),(17,1,3,NULL),(18,1,21,NULL),(19,1,26,NULL);
/*!40000 ALTER TABLE `user_material_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vocabulary`
--

DROP TABLE IF EXISTS `vocabulary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vocabulary` (
  `vocabulary_id` int NOT NULL,
  `level` int DEFAULT NULL,
  `word` varchar(50) NOT NULL,
  PRIMARY KEY (`vocabulary_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vocabulary`
--

LOCK TABLES `vocabulary` WRITE;
/*!40000 ALTER TABLE `vocabulary` DISABLE KEYS */;
/*!40000 ALTER TABLE `vocabulary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `word_meaning`
--

DROP TABLE IF EXISTS `word_meaning`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `word_meaning` (
  `meaning_id` int NOT NULL,
  `vocabulary_id` int NOT NULL,
  `meaning_text` varchar(100) NOT NULL,
  PRIMARY KEY (`meaning_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `word_meaning`
--

LOCK TABLES `word_meaning` WRITE;
/*!40000 ALTER TABLE `word_meaning` DISABLE KEYS */;
/*!40000 ALTER TABLE `word_meaning` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-14 11:46:06
