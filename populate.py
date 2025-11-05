#!/usr/bin/env python3
"""
Database population script for Daigaku application.
Populates the database with decks, flashcards, immersion materials, and history.
"""
import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
import random


def get_connection():
    """Create database connection."""
    try:
        connection = mysql.connector.connect(
            unix_socket='/tmp/mysql.sock',
            database='daigaku',
            user='root',
            password='root'
        )
        return connection
    except Error as e:
        print(f"❌ Error connecting to database: {e}")
        return None


def clear_existing_data(connection):
    """Clear existing data (except users)."""
    print("\n🗑️  Clearing existing data...")
    cursor = connection.cursor()
    
    try:
        # Clear in order due to foreign key constraints
        cursor.execute("DELETE FROM user_card_review")
        cursor.execute("DELETE FROM user_material_history")
        cursor.execute("DELETE FROM material_vocab_map")
        cursor.execute("DELETE FROM flashcard")
        cursor.execute("DELETE FROM deck")
        cursor.execute("DELETE FROM immersion_material")
        cursor.execute("DELETE FROM word_meaning")
        cursor.execute("DELETE FROM vocabulary")
        
        connection.commit()
        print("✓ Existing data cleared")
    except Error as e:
        print(f"❌ Error clearing data: {e}")
        connection.rollback()
    finally:
        cursor.close()


def populate_decks(connection):
    """Create JLPT decks N5 to N1."""
    print("\n📚 Creating JLPT decks...")
    cursor = connection.cursor()
    
    decks = [
        (1, "JLPT N5", "Beginner vocabulary - 50 cards", 5, 1),
        (2, "JLPT N4", "Elementary vocabulary - 50 cards", 4, 1),
        (3, "JLPT N3", "Intermediate vocabulary - 50 cards", 3, 1),
        (4, "JLPT N2", "Upper-intermediate vocabulary - 50 cards", 2, 1),
        (5, "JLPT N1", "Advanced vocabulary - 50 cards", 1, 1),
    ]
    
    try:
        cursor.executemany(
            "INSERT INTO deck (deck_id, deck_name, description, language_level, creator_id) VALUES (%s, %s, %s, %s, %s)",
            decks
        )
        connection.commit()
        print(f"✓ Created {len(decks)} decks")
    except Error as e:
        print(f"❌ Error creating decks: {e}")
        connection.rollback()
    finally:
        cursor.close()


def populate_flashcards(connection):
    """Create flashcards for each deck."""
    print("\n📇 Creating flashcards...")
    cursor = connection.cursor()
    
    # N5 Vocabulary (Beginner)
    n5_cards = [
        ("私", "I, me", "私は学生です。", "I am a student."),
        ("本", "book", "本を読みます。", "I read a book."),
        ("食べる", "to eat", "ご飯を食べます。", "I eat rice."),
        ("水", "water", "水を飲みます。", "I drink water."),
        ("学校", "school", "学校に行きます。", "I go to school."),
        ("友達", "friend", "友達と遊びます。", "I play with friends."),
        ("時間", "time", "時間がありません。", "I don't have time."),
        ("今日", "today", "今日は暑いです。", "It's hot today."),
        ("明日", "tomorrow", "明日会いましょう。", "Let's meet tomorrow."),
        ("昨日", "yesterday", "昨日映画を見ました。", "I watched a movie yesterday."),
        ("見る", "to see, watch", "テレビを見ます。", "I watch TV."),
        ("聞く", "to listen, hear", "音楽を聞きます。", "I listen to music."),
        ("話す", "to speak", "日本語を話します。", "I speak Japanese."),
        ("書く", "to write", "手紙を書きます。", "I write a letter."),
        ("読む", "to read", "新聞を読みます。", "I read the newspaper."),
        ("行く", "to go", "公園に行きます。", "I go to the park."),
        ("来る", "to come", "友達が来ます。", "My friend is coming."),
        ("帰る", "to return home", "家に帰ります。", "I return home."),
        ("買う", "to buy", "服を買います。", "I buy clothes."),
        ("売る", "to sell", "本を売ります。", "I sell books."),
        ("作る", "to make", "料理を作ります。", "I make food."),
        ("飲む", "to drink", "お茶を飲みます。", "I drink tea."),
        ("寝る", "to sleep", "早く寝ます。", "I sleep early."),
        ("起きる", "to wake up", "朝早く起きます。", "I wake up early in the morning."),
        ("勉強する", "to study", "日本語を勉強します。", "I study Japanese."),
        ("働く", "to work", "会社で働きます。", "I work at a company."),
        ("休む", "to rest", "土曜日に休みます。", "I rest on Saturday."),
        ("立つ", "to stand", "駅で立ちます。", "I stand at the station."),
        ("座る", "to sit", "椅子に座ります。", "I sit on a chair."),
        ("歩く", "to walk", "公園を歩きます。", "I walk in the park."),
        ("走る", "to run", "毎朝走ります。", "I run every morning."),
        ("乗る", "to ride", "電車に乗ります。", "I ride the train."),
        ("降りる", "to get off", "次の駅で降ります。", "I get off at the next station."),
        ("開ける", "to open", "窓を開けます。", "I open the window."),
        ("閉める", "to close", "ドアを閉めます。", "I close the door."),
        ("使う", "to use", "パソコンを使います。", "I use a computer."),
        ("入る", "to enter", "部屋に入ります。", "I enter the room."),
        ("出る", "to exit, leave", "家を出ます。", "I leave home."),
        ("会う", "to meet", "友達に会います。", "I meet a friend."),
        ("待つ", "to wait", "友達を待ちます。", "I wait for a friend."),
        ("持つ", "to hold, have", "かばんを持ちます。", "I hold a bag."),
        ("知る", "to know", "この人を知っています。", "I know this person."),
        ("分かる", "to understand", "日本語が分かります。", "I understand Japanese."),
        ("思う", "to think", "それは良いと思います。", "I think that's good."),
        ("言う", "to say", "何も言いません。", "I say nothing."),
        ("教える", "to teach", "英語を教えます。", "I teach English."),
        ("習う", "to learn", "ピアノを習います。", "I learn piano."),
        ("始める", "to begin", "勉強を始めます。", "I begin studying."),
        ("終わる", "to end", "授業が終わります。", "Class ends."),
        ("忘れる", "to forget", "名前を忘れました。", "I forgot the name."),
    ]
    
    # N4 Vocabulary (Elementary)
    n4_cards = [
        ("頑張る", "to do one's best", "試験を頑張ります。", "I'll do my best on the exam."),
        ("困る", "to be troubled", "お金がなくて困ります。", "I'm troubled because I have no money."),
        ("決める", "to decide", "旅行の日を決めます。", "I decide the travel date."),
        ("遊ぶ", "to play", "週末友達と遊びます。", "I play with friends on weekends."),
        ("笑う", "to laugh", "面白い話で笑います。", "I laugh at funny stories."),
        ("泣く", "to cry", "悲しい映画で泣きます。", "I cry at sad movies."),
        ("怒る", "to get angry", "彼は遅れて怒りました。", "He got angry about being late."),
        ("疲れる", "to get tired", "仕事で疲れます。", "I get tired from work."),
        ("選ぶ", "to choose", "好きな色を選びます。", "I choose my favorite color."),
        ("比べる", "to compare", "二つの商品を比べます。", "I compare two products."),
        ("変える", "to change", "予定を変えます。", "I change plans."),
        ("増える", "to increase", "人口が増えます。", "The population increases."),
        ("減る", "to decrease", "お金が減ります。", "Money decreases."),
        ("続ける", "to continue", "勉強を続けます。", "I continue studying."),
        ("止める", "to stop", "車を止めます。", "I stop the car."),
        ("付ける", "to attach, turn on", "電気を付けます。", "I turn on the light."),
        ("消す", "to turn off, erase", "電気を消します。", "I turn off the light."),
        ("壊れる", "to break", "時計が壊れました。", "The watch broke."),
        ("直す", "to fix, correct", "間違いを直します。", "I correct mistakes."),
        ("探す", "to search for", "鍵を探します。", "I search for keys."),
        ("見つける", "to find", "良い店を見つけます。", "I find a good store."),
        ("失う", "to lose", "大切なものを失いました。", "I lost something important."),
        ("拾う", "to pick up", "道で財布を拾いました。", "I picked up a wallet on the street."),
        ("捨てる", "to throw away", "ゴミを捨てます。", "I throw away trash."),
        ("貸す", "to lend", "友達に本を貸します。", "I lend a book to a friend."),
        ("借りる", "to borrow", "図書館で本を借ります。", "I borrow books from the library."),
        ("返す", "to return", "借りた本を返します。", "I return borrowed books."),
        ("送る", "to send", "メールを送ります。", "I send an email."),
        ("届く", "to reach, arrive", "荷物が届きました。", "The package arrived."),
        ("渡す", "to hand over", "プレゼントを渡します。", "I hand over a present."),
        ("もらう", "to receive", "お土産をもらいました。", "I received a souvenir."),
        ("あげる", "to give", "花をあげます。", "I give flowers."),
        ("くれる", "to give (to me)", "友達がくれました。", "My friend gave it to me."),
        ("助ける", "to help", "困っている人を助けます。", "I help people in trouble."),
        ("頼む", "to request, ask", "手伝いを頼みます。", "I ask for help."),
        ("誘う", "to invite", "パーティーに誘います。", "I invite to a party."),
        ("断る", "to refuse", "招待を断りました。", "I refused the invitation."),
        ("謝る", "to apologize", "遅れて謝ります。", "I apologize for being late."),
        ("褒める", "to praise", "良い仕事を褒めます。", "I praise good work."),
        ("注意する", "to warn, be careful", "危険に注意します。", "I'm careful of danger."),
        ("確認する", "to confirm", "予約を確認します。", "I confirm the reservation."),
        ("準備する", "to prepare", "旅行の準備をします。", "I prepare for the trip."),
        ("片付ける", "to tidy up", "部屋を片付けます。", "I tidy up the room."),
        ("掃除する", "to clean", "毎日掃除します。", "I clean every day."),
        ("洗う", "to wash", "手を洗います。", "I wash my hands."),
        ("拭く", "to wipe", "テーブルを拭きます。", "I wipe the table."),
        ("磨く", "to polish, brush", "歯を磨きます。", "I brush my teeth."),
        ("混む", "to be crowded", "電車が混みます。", "The train is crowded."),
        ("空く", "to become empty", "席が空きました。", "A seat became empty."),
        ("並ぶ", "to line up", "レジに並びます。", "I line up at the register."),
    ]
    
    # N3 Vocabulary (Intermediate)
    n3_cards = [
        ("達成する", "to achieve", "目標を達成しました。", "I achieved my goal."),
        ("実現する", "to realize", "夢を実現します。", "I realize my dream."),
        ("成功する", "to succeed", "ビジネスに成功しました。", "I succeeded in business."),
        ("失敗する", "to fail", "試験に失敗しました。", "I failed the exam."),
        ("発展する", "to develop", "技術が発展します。", "Technology develops."),
        ("進歩する", "to progress", "科学が進歩します。", "Science progresses."),
        ("向上する", "to improve", "成績が向上しました。", "My grades improved."),
        ("低下する", "to decline", "品質が低下します。", "Quality declines."),
        ("維持する", "to maintain", "健康を維持します。", "I maintain health."),
        ("保存する", "to preserve", "データを保存します。", "I save data."),
        ("破壊する", "to destroy", "環境を破壊します。", "Destroy the environment."),
        ("創造する", "to create", "新しいものを創造します。", "I create something new."),
        ("表現する", "to express", "気持ちを表現します。", "I express feelings."),
        ("理解する", "to understand", "意味を理解します。", "I understand the meaning."),
        ("説明する", "to explain", "ルールを説明します。", "I explain the rules."),
        ("証明する", "to prove", "理論を証明します。", "I prove the theory."),
        ("判断する", "to judge", "正しく判断します。", "I judge correctly."),
        ("評価する", "to evaluate", "結果を評価します。", "I evaluate the results."),
        ("批判する", "to criticize", "政策を批判します。", "I criticize policies."),
        ("賛成する", "to agree", "提案に賛成します。", "I agree with the proposal."),
        ("反対する", "to oppose", "計画に反対します。", "I oppose the plan."),
        ("主張する", "to insist", "意見を主張します。", "I insist on my opinion."),
        ("議論する", "to discuss", "問題を議論します。", "I discuss the problem."),
        ("協力する", "to cooperate", "チームで協力します。", "I cooperate with the team."),
        ("競争する", "to compete", "他社と競争します。", "I compete with other companies."),
        ("妥協する", "to compromise", "両方が妥協します。", "Both sides compromise."),
        ("克服する", "to overcome", "困難を克服します。", "I overcome difficulties."),
        ("解決する", "to solve", "問題を解決します。", "I solve problems."),
        ("対応する", "to respond", "要求に対応します。", "I respond to demands."),
        ("適応する", "to adapt", "環境に適応します。", "I adapt to the environment."),
        ("貢献する", "to contribute", "社会に貢献します。", "I contribute to society."),
        ("参加する", "to participate", "会議に参加します。", "I participate in meetings."),
        ("出席する", "to attend", "授業に出席します。", "I attend class."),
        ("欠席する", "to be absent", "学校を欠席しました。", "I was absent from school."),
        ("延期する", "to postpone", "会議を延期します。", "I postpone the meeting."),
        ("中止する", "to cancel", "イベントを中止します。", "I cancel the event."),
        ("実施する", "to implement", "計画を実施します。", "I implement the plan."),
        ("実行する", "to execute", "命令を実行します。", "I execute orders."),
        ("承認する", "to approve", "申請を承認します。", "I approve applications."),
        ("拒否する", "to reject", "要求を拒否します。", "I reject demands."),
        ("禁止する", "to prohibit", "喫煙を禁止します。", "I prohibit smoking."),
        ("許可する", "to permit", "使用を許可します。", "I permit usage."),
        ("命令する", "to order", "部下に命令します。", "I order subordinates."),
        ("要求する", "to demand", "改善を要求します。", "I demand improvements."),
        ("依頼する", "to request", "仕事を依頼します。", "I request work."),
        ("提案する", "to propose", "新しい案を提案します。", "I propose a new idea."),
        ("推薦する", "to recommend", "本を推薦します。", "I recommend books."),
        ("紹介する", "to introduce", "友人を紹介します。", "I introduce friends."),
        ("招待する", "to invite", "結婚式に招待します。", "I invite to a wedding."),
        ("案内する", "to guide", "道を案内します。", "I guide the way."),
    ]
    
    # N2 Vocabulary (Upper-intermediate)
    n2_cards = [
        ("抽象的", "abstract", "抽象的な概念です。", "It's an abstract concept."),
        ("具体的", "concrete", "具体的な例を示します。", "I show concrete examples."),
        ("複雑", "complex", "問題が複雑です。", "The problem is complex."),
        ("単純", "simple", "答えは単純です。", "The answer is simple."),
        ("曖昧", "ambiguous", "説明が曖昧です。", "The explanation is ambiguous."),
        ("明確", "clear", "意図が明確です。", "The intention is clear."),
        ("顕著", "remarkable", "変化が顕著です。", "The change is remarkable."),
        ("微妙", "subtle", "違いが微妙です。", "The difference is subtle."),
        ("深刻", "serious", "状況が深刻です。", "The situation is serious."),
        ("軽微", "minor", "被害は軽微です。", "The damage is minor."),
        ("重大", "grave", "重大な問題です。", "It's a grave problem."),
        ("些細", "trivial", "些細なことです。", "It's a trivial matter."),
        ("膨大", "enormous", "データが膨大です。", "The data is enormous."),
        ("僅か", "slight", "僅かな差です。", "It's a slight difference."),
        ("著しい", "notable", "進歩が著しいです。", "Progress is notable."),
        ("顕在化する", "to become apparent", "問題が顕在化しました。", "The problem became apparent."),
        ("潜在的", "latent", "潜在的な危険があります。", "There's latent danger."),
        ("根本的", "fundamental", "根本的な解決が必要です。", "A fundamental solution is needed."),
        ("表面的", "superficial", "理解が表面的です。", "Understanding is superficial."),
        ("本質的", "essential", "本質的な問題です。", "It's an essential problem."),
        ("一時的", "temporary", "一時的な措置です。", "It's a temporary measure."),
        ("永続的", "permanent", "永続的な平和を望みます。", "I wish for permanent peace."),
        ("相対的", "relative", "価値は相対的です。", "Value is relative."),
        ("絶対的", "absolute", "絶対的な真実です。", "It's an absolute truth."),
        ("包括的", "comprehensive", "包括的な調査です。", "It's a comprehensive survey."),
        ("限定的", "limited", "効果は限定的です。", "The effect is limited."),
        ("普遍的", "universal", "普遍的な法則です。", "It's a universal law."),
        ("特殊", "special", "特殊な状況です。", "It's a special situation."),
        ("一般的", "general", "一般的な意見です。", "It's a general opinion."),
        ("個別", "individual", "個別に対応します。", "I respond individually."),
        ("統一する", "to unify", "規格を統一します。", "I unify standards."),
        ("分割する", "to divide", "作業を分割します。", "I divide the work."),
        ("統合する", "to integrate", "システムを統合します。", "I integrate systems."),
        ("分離する", "to separate", "物質を分離します。", "I separate substances."),
        ("融合する", "to fuse", "文化が融合します。", "Cultures fuse."),
        ("独立する", "to be independent", "会社から独立しました。", "I became independent from the company."),
        ("依存する", "to depend", "輸入に依存します。", "I depend on imports."),
        ("関連する", "to relate", "事件に関連します。", "It relates to the incident."),
        ("無関係", "unrelated", "二つは無関係です。", "The two are unrelated."),
        ("直接", "direct", "直接話します。", "I speak directly."),
        ("間接的", "indirect", "間接的な影響です。", "It's an indirect influence."),
        ("積極的", "positive", "積極的に参加します。", "I participate actively."),
        ("消極的", "passive", "態度が消極的です。", "The attitude is passive."),
        ("能動的", "active", "能動的に動きます。", "I act actively."),
        ("受動的", "passive", "受動的な姿勢です。", "It's a passive posture."),
        ("自発的", "voluntary", "自発的に手伝います。", "I help voluntarily."),
        ("強制的", "compulsory", "強制的な措置です。", "It's a compulsory measure."),
        ("意図的", "intentional", "意図的な行動です。", "It's intentional behavior."),
        ("偶然", "accidental", "偶然の出会いです。", "It's an accidental meeting."),
        ("必然的", "inevitable", "結果は必然的です。", "The result is inevitable."),
    ]
    
    # N1 Vocabulary (Advanced)
    n1_cards = [
        ("錯綜する", "to be complicated", "情報が錯綜しています。", "Information is complicated."),
        ("紛糾する", "to be in a tangle", "議論が紛糾しました。", "The discussion got tangled."),
        ("煩雑", "troublesome", "手続きが煩雑です。", "Procedures are troublesome."),
        ("繁雑", "intricate", "作業が繁雑です。", "The work is intricate."),
        ("緻密", "meticulous", "計画が緻密です。", "The plan is meticulous."),
        ("粗雑", "rough", "仕事が粗雑です。", "The work is rough."),
        ("精巧", "elaborate", "細工が精巧です。", "The craft is elaborate."),
        ("粗悪", "inferior", "品質が粗悪です。", "Quality is inferior."),
        ("卓越する", "to excel", "技術に卓越しています。", "I excel in technology."),
        ("凡庸", "mediocre", "能力が凡庸です。", "Ability is mediocre."),
        ("顕著", "conspicuous", "効果が顕著です。", "The effect is conspicuous."),
        ("希薄", "thin", "関係が希薄です。", "The relationship is thin."),
        ("濃密", "dense", "時間が濃密です。", "Time is dense."),
        ("希少", "rare", "資源が希少です。", "Resources are rare."),
        ("豊富", "abundant", "経験が豊富です。", "Experience is abundant."),
        ("欠乏する", "to lack", "栄養が欠乏します。", "Nutrition is lacking."),
        ("充足する", "to be satisfied", "条件が充足します。", "Conditions are satisfied."),
        ("飽和する", "to be saturated", "市場が飽和しました。", "The market is saturated."),
        ("枯渇する", "to be exhausted", "資源が枯渇します。", "Resources are exhausted."),
        ("蓄積する", "to accumulate", "知識が蓄積します。", "Knowledge accumulates."),
        ("消耗する", "to be worn out", "体力が消耗します。", "Physical strength wears out."),
        ("補充する", "to replenish", "在庫を補充します。", "I replenish inventory."),
        ("補完する", "to complement", "互いに補完します。", "We complement each other."),
        ("代替する", "to substitute", "製品を代替します。", "I substitute products."),
        ("模倣する", "to imitate", "デザインを模倣します。", "I imitate designs."),
        ("創出する", "to create", "価値を創出します。", "I create value."),
        ("派生する", "to derive", "問題が派生します。", "Problems derive."),
        ("誘発する", "to induce", "反応を誘発します。", "I induce reactions."),
        ("抑制する", "to suppress", "欲望を抑制します。", "I suppress desires."),
        ("促進する", "to promote", "成長を促進します。", "I promote growth."),
        ("阻害する", "to hinder", "進歩を阻害します。", "I hinder progress."),
        ("妨害する", "to obstruct", "計画を妨害します。", "I obstruct plans."),
        ("擁護する", "to defend", "権利を擁護します。", "I defend rights."),
        ("攻撃する", "to attack", "敵を攻撃します。", "I attack enemies."),
        ("防御する", "to defend", "国を防御します。", "I defend the country."),
        ("侵害する", "to infringe", "著作権を侵害します。", "I infringe copyright."),
        ("遵守する", "to observe", "法律を遵守します。", "I observe laws."),
        ("違反する", "to violate", "規則に違反します。", "I violate rules."),
        ("逸脱する", "to deviate", "基準から逸脱します。", "I deviate from standards."),
        ("遭遇する", "to encounter", "困難に遭遇します。", "I encounter difficulties."),
        ("直面する", "to face", "危機に直面します。", "I face a crisis."),
        ("回避する", "to avoid", "リスクを回避します。", "I avoid risks."),
        ("克服する", "to overcome", "障害を克服します。", "I overcome obstacles."),
        ("凌駕する", "to surpass", "期待を凌駕します。", "I surpass expectations."),
        ("匹敵する", "to rival", "実力が匹敵します。", "Abilities rival."),
        ("劣る", "to be inferior", "品質が劣ります。", "Quality is inferior."),
        ("勝る", "to be superior", "性能が勝ります。", "Performance is superior."),
        ("凌ぐ", "to surpass", "前作を凌ぎます。", "I surpass the previous work."),
        ("追随する", "to follow", "流行に追随します。", "I follow trends."),
        ("先駆ける", "to pioneer", "分野を先駆けます。", "I pioneer the field."),
    ]
    
    all_cards = []
    card_id = 1
    
    # Add N5 cards
    for expr, definition, jp_sent, en_trans in n5_cards:
        all_cards.append((card_id, 1, expr, definition, jp_sent, en_trans))
        card_id += 1
    
    # Add N4 cards
    for expr, definition, jp_sent, en_trans in n4_cards:
        all_cards.append((card_id, 2, expr, definition, jp_sent, en_trans))
        card_id += 1
    
    # Add N3 cards
    for expr, definition, jp_sent, en_trans in n3_cards:
        all_cards.append((card_id, 3, expr, definition, jp_sent, en_trans))
        card_id += 1
    
    # Add N2 cards
    for expr, definition, jp_sent, en_trans in n2_cards:
        all_cards.append((card_id, 4, expr, definition, jp_sent, en_trans))
        card_id += 1
    
    # Add N1 cards
    for expr, definition, jp_sent, en_trans in n1_cards:
        all_cards.append((card_id, 5, expr, definition, jp_sent, en_trans))
        card_id += 1
    
    try:
        cursor.executemany(
            """INSERT INTO flashcard 
               (card_id, deck_id, expression, expression_definition, japanese_sentence, english_translation) 
               VALUES (%s, %s, %s, %s, %s, %s)""",
            all_cards
        )
        connection.commit()
        print(f"✓ Created {len(all_cards)} flashcards across all decks")
    except Error as e:
        print(f"❌ Error creating flashcards: {e}")
        connection.rollback()
    finally:
        cursor.close()


def populate_immersion_materials(connection):
    """Create immersion materials based on popular anime and Japanese content."""
    print("\n🎬 Creating immersion materials...")
    cursor = connection.cursor()
    
    materials = [
        # Anime - Television
        (1, "Naruto", "https://www.crunchyroll.com/naruto", "television", "Crunchyroll", 480, 3),
        (2, "Attack on Titan", "https://www.crunchyroll.com/attack-on-titan", "television", "Crunchyroll", 300, 4),
        (3, "One Piece", "https://www.crunchyroll.com/one-piece", "television", "Crunchyroll", 12000, 3),
        (4, "Death Note", "https://www.netflix.com/death-note", "television", "Netflix", 552, 4),
        (5, "Demon Slayer", "https://www.crunchyroll.com/demon-slayer", "television", "Crunchyroll", 312, 3),
        (6, "My Hero Academia", "https://www.crunchyroll.com/my-hero-academia", "television", "Crunchyroll", 720, 3),
        (7, "Steins;Gate", "https://www.crunchyroll.com/steinsgate", "television", "Crunchyroll", 600, 4),
        (8, "Fullmetal Alchemist", "https://www.crunchyroll.com/fullmetal-alchemist", "television", "Crunchyroll", 1560, 4),
        (9, "Sword Art Online", "https://www.crunchyroll.com/sword-art-online", "television", "Crunchyroll", 1200, 3),
        (10, "Tokyo Ghoul", "https://www.crunchyroll.com/tokyo-ghoul", "television", "Crunchyroll", 576, 4),
        
        # Anime - Movies
        (11, "Your Name", "https://www.crunchyroll.com/your-name", "movie", "Crunchyroll", 106, 3),
        (12, "Spirited Away", "https://www.hbomax.com/spirited-away", "movie", "HBO Max", 125, 3),
        (13, "A Silent Voice", "https://www.netflix.com/a-silent-voice", "movie", "Netflix", 130, 4),
        (14, "Weathering With You", "https://www.crunchyroll.com/weathering-with-you", "movie", "Crunchyroll", 114, 3),
        (15, "Howl's Moving Castle", "https://www.hbomax.com/howls-moving-castle", "movie", "HBO Max", 119, 3),
        
        # Books
        (16, "Norwegian Wood", "https://www.amazon.com/norwegian-wood", "book", "Amazon", None, 4),
        (17, "Kitchen", "https://www.amazon.com/kitchen-banana", "book", "Amazon", None, 3),
        (18, "1Q84", "https://www.amazon.com/1q84", "book", "Amazon", None, 5),
        (19, "Battle Royale", "https://www.amazon.com/battle-royale", "book", "Amazon", None, 4),
        (20, "Kafka on the Shore", "https://www.amazon.com/kafka-shore", "book", "Amazon", None, 5),
        
        # Podcasts
        (21, "JapanesePod101", "https://www.japanesepod101.com", "podcast", "JapanesePod101", 30, 2),
        (22, "NHK Easy Japanese", "https://www.nhk.or.jp/lesson", "podcast", "NHK", 20, 2),
        (23, "Learn Japanese Pod", "https://www.learnjapanesepod.com", "podcast", "Learn Japanese Pod", 45, 3),
        (24, "Nihongo con Teppei", "https://nihongoconteppei.com", "podcast", "Teppei Sensei", 15, 3),
        (25, "Bilingual News", "https://bilingualnews.jp", "podcast", "Bilingual News", 60, 4),
    ]
    
    try:
        cursor.executemany(
            """INSERT INTO immersion_material 
               (material_id, title, purchase_website_url, type, source, length, average_difficulty) 
               VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            materials
        )
        connection.commit()
        print(f"✓ Created {len(materials)} immersion materials")
    except Error as e:
        print(f"❌ Error creating immersion materials: {e}")
        connection.rollback()
    finally:
        cursor.close()


def populate_user_history(connection):
    """Create user material history for both users."""
    print("\n📝 Creating user immersion history...")
    cursor = connection.cursor()
    
    # Root user watches mostly advanced content
    root_history = [
        (1, 1, 1, None),  # Naruto
        (2, 1, 2, None),  # Attack on Titan
        (3, 1, 4, "Want to rewatch"),  # Death Note
        (4, 1, 5, None),  # Demon Slayer
        (5, 1, 11, "Favorite movie"),  # Your Name
        (6, 1, 12, None),  # Spirited Away
        (7, 1, 18, "Reading now"),  # 1Q84
        (8, 1, 25, None),  # Bilingual News
    ]
    
    # Customer user watches beginner-friendly content
    customer_history = [
        (9, 2, 1, None),  # Naruto
        (10, 2, 5, "Currently watching"),  # Demon Slayer
        (11, 2, 6, None),  # My Hero Academia
        (12, 2, 11, "Watched 3 times"),  # Your Name
        (13, 2, 14, None),  # Weathering With You
        (14, 2, 17, "First Japanese book"),  # Kitchen
        (15, 2, 21, "Daily listening"),  # JapanesePod101
        (16, 2, 22, None),  # NHK Easy Japanese
    ]
    
    all_history = root_history + customer_history
    
    try:
        cursor.executemany(
            """INSERT INTO user_material_history 
               (history_id, user_id, material_id, saved_for_later) 
               VALUES (%s, %s, %s, %s)""",
            all_history
        )
        connection.commit()
        print(f"✓ Created {len(all_history)} history entries")
    except Error as e:
        print(f"❌ Error creating user history: {e}")
        connection.rollback()
    finally:
        cursor.close()


def populate_review_history(connection):
    """Create some sample review history for both users."""
    print("\n⭐ Creating review history...")
    cursor = connection.cursor()
    
    reviews = []
    review_id = 1
    
    # Root user has reviewed many N5 cards
    for card_id in range(1, 26):  # First 25 N5 cards
        quality = random.randint(3, 5)  # Good performance
        reviews.append((review_id, 1, card_id, datetime.now().date(), quality, datetime.now()))
        review_id += 1
    
    # Customer user has reviewed some N5 cards
    for card_id in range(1, 11):  # First 10 N5 cards
        quality = random.randint(2, 4)  # Mixed performance
        reviews.append((review_id, 2, card_id, datetime.now().date(), quality, datetime.now()))
        review_id += 1
    
    try:
        cursor.executemany(
            """INSERT INTO user_card_review 
               (review_id, user_id, card_id, review_date, answer_quality, time_taken) 
               VALUES (%s, %s, %s, %s, %s, %s)""",
            reviews
        )
        connection.commit()
        print(f"✓ Created {len(reviews)} review records")
    except Error as e:
        print(f"❌ Error creating review history: {e}")
        connection.rollback()
    finally:
        cursor.close()


def print_summary(connection):
    """Print summary of database contents."""
    print("\n" + "=" * 60)
    print("DATABASE POPULATION SUMMARY")
    print("=" * 60)
    
    cursor = connection.cursor()
    
    # Count decks
    cursor.execute("SELECT COUNT(*) FROM deck")
    deck_count = cursor.fetchone()[0]
    print(f"\n📚 Decks: {deck_count}")
    
    # Count flashcards per deck
    cursor.execute("""
        SELECT d.deck_name, COUNT(f.card_id) 
        FROM deck d 
        LEFT JOIN flashcard f ON d.deck_id = f.deck_id 
        GROUP BY d.deck_id
    """)
    for deck_name, count in cursor.fetchall():
        print(f"   • {deck_name}: {count} cards")
    
    # Count immersion materials
    cursor.execute("SELECT COUNT(*) FROM immersion_material")
    material_count = cursor.fetchone()[0]
    print(f"\n🎬 Immersion Materials: {material_count}")
    
    cursor.execute("""
        SELECT type, COUNT(*) 
        FROM immersion_material 
        GROUP BY type
    """)
    for mat_type, count in cursor.fetchall():
        print(f"   • {mat_type.capitalize()}: {count}")
    
    # Count user history
    cursor.execute("""
        SELECT u.username, COUNT(umh.history_id) 
        FROM user u 
        LEFT JOIN user_material_history umh ON u.user_id = umh.user_id 
        GROUP BY u.user_id
    """)
    print(f"\n📝 User History:")
    for username, count in cursor.fetchall():
        print(f"   • {username}: {count} materials logged")
    
    # Count reviews
    cursor.execute("""
        SELECT u.username, COUNT(ucr.review_id) 
        FROM user u 
        LEFT JOIN user_card_review ucr ON u.user_id = ucr.user_id 
        GROUP BY u.user_id
    """)
    print(f"\n⭐ Card Reviews:")
    for username, count in cursor.fetchall():
        print(f"   • {username}: {count} reviews")
    
    cursor.close()
    
    print("\n" + "=" * 60)
    print("✅ DATABASE POPULATION COMPLETE!")
    print("=" * 60)


def main():
    """Main function to populate the database."""
    print("=" * 60)
    print("DAIGAKU DATABASE POPULATION SCRIPT")
    print("=" * 60)
    
    connection = get_connection()
    if not connection:
        return
    
    try:
        clear_existing_data(connection)
        populate_decks(connection)
        populate_flashcards(connection)
        populate_immersion_materials(connection)
        populate_user_history(connection)
        populate_review_history(connection)
        print_summary(connection)
        
        print("\n🎉 You can now run: python3 main.py")
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
