# static_qa_data.py - 静的なQ&Aデータと文脈に応じた提案機能（金彩職人版）

# ==========================================
# 🐶 金彩職人向けQ&Aデータ（言語別）
# ========================================== 

# ====================================================================
# 🎯 メディアデータ（画像・動画・リンク）
# ====================================================================
# 注意: 疑問符（？）はget_qa_media関数で自動正規化されるため不要

qa_media_data = {
    # 日本語版
    "金彩って何": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/kinsai.png",
                "caption": "金彩が施された京友禅の着物です",
                "alt": "京友禅の美しい着物"
            }
        ]
    },
    
    "道具は何を使うの": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/sunagotutu.png",
                "caption": "砂子筒などの金彩で使う道具ですワン",
                "alt": "金彩の道具"
            }
        ]
    },
    
    "金線描きって何": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/kikukuri.png",
                "caption": "金線描きで描かれた繊細な模様です",
                "alt": "金線描きの技法"
            }
        ]
    },
    
    "押し箔ってどうやるの": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/osihaku.png",
                "caption": "押し箔で金箔を貼っている様子ですワン",
                "alt": "押し箔の技法"
            }
        ]
    },
    
    "摺箔って何": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/surihaku.png",
                "caption": "摺箔で型紙を使って文様を写しています",
                "alt": "摺箔の技法"
            }
        ]
    },
    
    # 英語版
    "What is Kinsai": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/kinsai.png",
                "caption": "Kimono with Kinsai gold decoration! Woof!",
                "alt": "Beautiful Kyo-Yuzen kimono"
            }
        ]
    },
    
    "What tools do you use": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/sunagotutu.png",
                "caption": "Various tools like Sunago-zutsu used in Kinsai! Woof!",
                "alt": "Kinsai tools"
            }
        ]
    },
    
    "What is Kinsen-gaki": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/kikukuri.png",
                "caption": "Delicate patterns drawn with Kinsen-gaki",
                "alt": "Kinsen-gaki technique"
            }
        ]
    },
    
    "How do you do Oshi-haku": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/osihaku.png",
                "caption": "Applying gold leaf with Oshi-haku! Woof!",
                "alt": "Oshi-haku technique"
            }
        ]
    },
    
    "What is Surihaku": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/surihaku.png",
                "caption": "Transferring patterns using stencils with Surihaku",
                "alt": "Surihaku technique"
            }
        ]
    },
}

qa_responses = {
    'ja': {
        # Phase1: 金彩の概要・基本
        'phase1_overview': {
            "金彩って何": """
                金彩っていうのは、染め上がった生地に金や銀の箔を貼り付けて装飾する技術です。
                
                友禅染めだけだとちょっとボヤっとした印象になることがあるんだけど、そこに金彩でキリッと仕上げるんですワン。だから「化粧係」って呼ばれてるんですよ。
                
               京友禅の華やかさを決める大事な工程になってます。
                [EMOTION:happy]
            """,
            
            "道具は何を使うの": """
                いろいろあるんだけど、一番大事なのは「砂子筒」かな。竹筒に金網を張った道具で、これで金を振り落とすんです。
                
                なぜ竹かって？静電気が起きにくいんですよ。金箔って本当に繊細で、指で触ったら一発でくっついてダメになっちゃう。だから箔を掴む「箔箸」も竹製なんです。
                
                僕は100本くらいの砂子筒を使い分けてますワン。網目の粗さによって金の粒の大きさが変わるから、それぞれ用途が違うんです。
                [EMOTION:neutral]
            """
        },
        
        # Phase2: 技術詳細の掘り下げ
        'phase2_technical': {
            "金線描きって何": """
                金線描きは、筒の先から金を絞り出して線を描く技法です。「金くくり」とか「筒描き」とも呼ばれてるんですワン。
                
                友禅染めの糸目糊の上に金の線を描くことが多くて、細い輪郭線や細かい装飾に使います。均一な線を描くには集中力が必要で、繊細な作業なんです。
                
                料理で言うと、ケーキにチョコペンで文字を書くみたいな感じですかね。手元が狂うと台無しになっちゃいます。
                [EMOTION:neutral]
            """,
            
            "押し箔ってどうやるの": """
                押し箔は、広い面積に金箔を均一に貼る技法です。「ベタ箔」とも呼ばれてますワン。
                
                まずマスキングシートを彫り抜いて、接着剤を塗って、竹製の箔箸で金箔をシワなく貼っていきます。接着剤のムラやシワがあると仕上がりに影響するから、丁寧に作業するのがポイントです。
                
                うまくいくと豪華な仕上がりになるんですよ。金箔がピカーッと輝いて、本当に綺麗なんです！
                [EMOTION:happy]
            """,
            
            "摺箔って何": """
                摺箔は、型紙を使って文様を写す技法です。シルクスクリーンを置いて、接着剤をヘラで塗って、金箔を置くと型紙通りの文様が現れるんですワン。
                
                昭和初期からの伝統的な型紙もあるし、新しいデザインの型もあって、いろんな文様ができるんです。型紙の位置合わせと、接着剤を均一に塗るのが腕の見せどころですね。
                
                型紙があれば同じ文様を何度も作れるから、再現性が高いんです。これが僕の好きなところ！
                [EMOTION:happy]
            """,
            
            "砂子ってどうやって振るの": """
                砂子は、竹筒に金網を張った砂子筒に箔を入れて、トントンと叩いて振り落とす技法です。「振金」とも呼ばれてますワン。
                
                金網の番手で箔の細かさを調整できるんです。大きい穴なら大粒、小さい穴なら細かい金が出る。料理で塩を振るのと同じ感覚ですね。
                
                漆器の蒔絵みたいなキラキラした質感が出せるんですよ。筒を叩く力加減と、均一に散らす技術が大事なんです。何年やっても楽しいです！
                [EMOTION:happy]
            """,
        },
        
        # Phase3: パーソナルな部分
        'phase3_personal': {
            "職人として一番苦労したことは": """
                修行時代は大変でしたね...金箔って本当にフワフワで軽いんです。ちょっと「ハァー」って息を吐いただけで飛んでいっちゃう。
                
                緊張で手がブルブル震えた日には、もう終わりです。何時間もかけた仕事が一瞬でパーになる。何度泣きそうになったことか...
                
                でもある日突然「あれ？できた！」って瞬間が来るんですよ。その時は嬉しくて嬉しくて。先輩に「おお、やっとできたな」って言われて、すごく感動しました。今でもあの時のこと、忘れられないですね。
                [EMOTION:sad]
            """,
            
            "仕事以外で好きなことは": """
                実は温泉が大好きなんです！金彩の仕事はずっと細かい作業で、気づいたら肩がガチガチになってるんですワン。
                
                だから温泉に入って、「あぁ〜極楽極楽」ってゆっくりするのが最高なんです。体も心もホカホカになりますよ。
                
                あと散歩も大好きです。京都の街をブラブラ歩いて、「あ、桜が咲いてる」とか「紅葉が綺麗だな」って季節を感じるのが楽しいんです。綺麗な景色を見つけると、つい写真をパシャパシャ撮っちゃいますね。
                [EMOTION:happy]
            """,
            
            "金彩の魅力を一言で言うと": """
                「手仕事の温かさ」ですかね。機械では出せない、人の手が生み出す柔らかさや個性があるんです。
                
                一つ一つの着物が唯一無二で、作り手の想いが込められている。それが金彩の魅力だと思いますワン。
                
                伝統を守りながら、新しい挑戦もしていきたいですね。あと、教えることも視野に入れないといけないと思い始めてます。
                [EMOTION:happy]
            """,
        }
    },
    
    'en': {
        # Phase1: Overview & Basics
        'phase1_overview': {
            "What is Kinsai": """
                Kinsai is the technique of applying gold and silver leaf to dyed fabric for decoration.
                
                Yuzen dyeing alone can look a bit soft, so we use Kinsai to sharpen it up! That's why we're called the "Makeup crew." Woof!
                
                This started in the Meiji era around 1897, and now it's a super important part of Kyo-Yuzen kimono, giving them that gorgeous sparkle.
                [EMOTION:happy]
            """,
            
            "What tools do you use": """
                There are lots of tools, but the most important is the "Sunago-zutsu" - a bamboo tube with a metal mesh.
                
                Why bamboo? Because gold leaf is super light and sticks to everything with static electricity! Bamboo doesn't make static. Smart, right? The "Haku-bashi" (leaf chopsticks) for picking up the leaf are also bamboo.
                
                I have about 100 different Sunago-zutsu. The mesh size changes the gold particle size, so each one has a different purpose. Woof!
                [EMOTION:neutral]
            """
        },
        
        # Phase2: Technical Details
        'phase2_technical': {
            "What is Kinsen-gaki": """
                Kinsen-gaki is a technique where you squeeze gold out from a tube tip to draw lines. It's also called "Kin-kukuri" or "Tsutsu-gaki." Woof!
                
                We often draw gold lines over the itome-nori (rice paste lines) in Yuzen dyeing. It's used for fine outlines and detailed decorations. You need concentration to draw uniform lines - it's delicate work.
                
                It's like writing on a cake with chocolate pen, you know? If your hand slips, it's ruined!
                [EMOTION:neutral]
            """,
            
            "How do you do Oshi-haku": """
                Oshi-haku is a technique to apply gold leaf uniformly over a large area. It's also called "Beta-haku." Woof!
                
                First, you carve out a masking sheet, apply glue, then use bamboo leaf-chopsticks to stick the gold leaf without wrinkles. If there's uneven glue or wrinkles, it affects the finish, so careful work is key.
                
                When it works well, it's gorgeous! The gold leaf shines so bright and beautiful!
                [EMOTION:happy]
            """,
            
            "What is Surihaku": """
                Surihaku is a technique using stencils to transfer patterns. You place Ise stencils or silk screens, spread glue with a spatula, and when you put gold leaf on, the stencil pattern appears! Woof!
                
                There are traditional stencils from the early Showa period and new design stencils too, so you can make various patterns. Aligning the stencil and spreading glue evenly is where skill matters.
                
                With stencils, you can make the same pattern repeatedly, so it has high reproducibility. That's what I love about it!
                [EMOTION:happy]
            """,
            
            "How do you do Sunago": """
                Sunago is a technique where you put leaf in a bamboo tube with metal mesh (sunago-zutsu) and tap-tap to sprinkle it down. It's also called "Furikin." Woof!
                
                You can adjust the fineness of the leaf with the mesh number. Big holes make large grains, small holes make fine gold. Same feeling as sprinkling salt in cooking!
                
                It creates glittery texture like lacquerware maki-e. The strength of tapping and the technique to scatter evenly are important. Fun no matter how many years I do it!
                [EMOTION:happy]
            """,
        },
        
        # Phase3: Personal
        'phase3_personal': {
            "What was your biggest challenge as a craftsperson": """
                Oh, my apprenticeship days were tough... Gold leaf is so light and floaty! Just go "haaa" with your breath and whoosh - it flies away!
                
                When my hands trembled from nerves, that was it. Hours of work gone in a second. I wanted to cry so many times...
                
                But you know what? One day suddenly "Wait, I did it!" moment comes! Woof! I was so happy and excited! My senior said "Finally, you got it" and I was so moved. I'll never forget that feeling!
                [EMOTION:sad]
            """,
            
            "What do you like to do besides work": """
                Actually, I LOVE hot springs! You know, doing detailed work all day makes my shoulders super stiff. Woof!
                
                So soaking in a hot spring going "Ahhh, this is heaven" is the BEST! Makes my body and soul feel warm and happy!
                
                I also love walking around! Strolling through Kyoto streets and noticing "Oh, cherry blossoms are blooming!" or "Wow, the autumn leaves are beautiful!" - feeling the seasons is so fun! When I see something pretty, I can't help but snap photos.
                [EMOTION:happy]
            """,
            
            "What's the charm of Kinsai in one word": """
                "The warmth of handmade work." There's a softness and individuality created by human hands that machines can't produce.
                
                Each kimono is unique, and the maker's feelings are put into it - that's the charm of Kinsai I think. Woof!
                
                I want to continue protecting tradition while also taking on new challenges. And I'm also thinking about teaching the next generation.
                [EMOTION:happy]
            """,
        }
    }
}

# サジェスチョン（言語別・Phase別）
suggestions = {
    'ja': {
        'phase1_overview': [
            "金彩って何？",
            "道具は何を使うの？",
        ],
        'phase2_technical': [
            "金線描きって何？",
            "押し箔ってどうやるの？",
            "摺箔って何？",
            "砂子ってどうやって振るの？",
        ],
        'phase3_personal': [
            "職人として一番苦労したことは？",
            "仕事以外で好きなことは？",
        ]
    },
    'en': {
        'phase1_overview': [
            "What is Kinsai?",
            "What tools do you use?",
        ],
        'phase2_technical': [
            "What is Kinsen-gaki?",
            "How do you do Oshi-haku?",
            "What is Surihaku?",
            "How do you do Sunago?",
        ],
        'phase3_personal': [
            "What was your biggest challenge as a craftsperson?",
            "What do you like to do besides work?",
        ]
    }
}

# ==========================================
# 汎用関数（金彩職人用）
# ==========================================

def get_current_phase(selected_count):
    """
    選択されたサジェスチョン数から現在のPhaseを判定
    
    Args:
        selected_count: 選択されたサジェスチョン数
    
    Returns:
        str: 現在のPhase ('phase1_overview', 'phase2_technical', 'phase3_personal')
    """
    # Phase1: 2個、Phase2: 4個、Phase3: それ以降
    if selected_count < 2:  # 0, 1 → Phase1
        return 'phase1_overview'
    elif selected_count < 6:  # 2, 3, 4, 5 → Phase2
        return 'phase2_technical'
    else:  # 6以上 → Phase3
        return 'phase3_personal'

def get_suggestions_for_phase(phase, selected_suggestions, user_type='default', language='ja'):
    """
    Phaseに応じたサジェスチョンを取得（金彩職人用）
    
    Args:
        phase: 現在のPhase
        selected_suggestions: 既に選択されたサジェスチョンのリスト
        user_type: ユーザータイプ（金彩職人用では使用しない）
        language: 言語 ('ja' or 'en')
    
    Returns:
        list: サジェスチョンのリスト
    """
    # 言語に応じたサジェスチョンを取得
    lang_suggestions = suggestions.get(language, suggestions['ja'])
    phase_suggestions = lang_suggestions.get(phase, [])
    
    # 既に選択されたものを除外
    available_suggestions = [s for s in phase_suggestions if s not in selected_suggestions]
    
    return available_suggestions

def get_response_for_user(message, user_type='default', current_phase='phase1_overview', language='ja'):
    """
    ユーザーのメッセージに対する応答を取得（金彩職人用）
    
    Args:
        message: ユーザーのメッセージ
        user_type: ユーザータイプ（金彩職人用では使用しない）
        current_phase: 現在のPhase
        language: 言語 ('ja' or 'en')
    
    Returns:
        dict or None: 応答データ（見つかった場合）
    """
    # 正規化（小文字化、空白削除）
    normalized_message = message.lower().replace(' ', '').replace('　', '').replace('？', '').replace('?', '')
    
    # 言語に応じたQ&Aデータを取得
    lang_qa = qa_responses.get(language, qa_responses['ja'])
    
    # 現在のPhaseのQ&Aデータを取得
    phase_qa = lang_qa.get(current_phase, {})
    
    # 完全一致チェック
    for key, response in phase_qa.items():
        normalized_key = key.lower().replace(' ', '').replace('　', '')
        if normalized_key in normalized_message or normalized_message in normalized_key:
            return parse_response(response)
    
    # 全Phase横断検索
    for phase_name, qa_dict in lang_qa.items():
        for key, response in qa_dict.items():
            normalized_key = key.lower().replace(' ', '').replace('　', '')
            if normalized_key in normalized_message or normalized_message in normalized_key:
                return parse_response(response)
    
    return None

def parse_response(response_text):
    """
    応答テキストから感情タグを抽出
    
    Args:
        response_text: 応答テキスト
    
    Returns:
        dict: {'text': str, 'emotion': str}
    """
    import re
    
    # [EMOTION:xxx] タグを検索
    emotion_match = re.search(r'\[EMOTION:(\w+)\]', response_text)
    emotion = emotion_match.group(1) if emotion_match else 'neutral'
    
    # テキストから感情タグを削除
    clean_text = re.sub(r'\[EMOTION:\w+\]', '', response_text).strip()
    
    return {
        'text': clean_text,
        'emotion': emotion
    }

def get_qa_media(question):
    """
    質問に紐付くメディアデータを取得
    
    Args:
        question (str): 質問テキスト
        
    Returns:
        dict or None: メディアデータ、存在しない場合はNone
    """
    if not question or not qa_media_data:
        return None
    
    # 完全一致チェック（最も高速）
    if question in qa_media_data:
        print(f"📷 メディアヒット（完全一致）: {question}")
        return qa_media_data[question]
    
    # 正規化して完全一致チェック
    question_normalized = question.replace('?', '').replace('？', '').strip()
    
    for key in qa_media_data.keys():
        key_normalized = key.replace('?', '').replace('？', '').strip()
        if question_normalized == key_normalized:
            print(f"📷 メディアヒット（正規化一致）: {key}")
            return qa_media_data[key]
    
    # 部分一致チェック（フォールバック）
    question_lower = question_normalized.lower().replace(' ', '').replace('　', '')
    
    for key, media_data in qa_media_data.items():
        key_lower = key.replace('?', '').replace('？', '').strip().lower().replace(' ', '').replace('　', '')
        
        # キーワードマッチング
        if key_lower in question_lower or question_lower in key_lower:
            # メディアがある場合のみ返す
            if media_data.get('images') or media_data.get('videos') or media_data.get('link'):
                print(f"📷 メディアヒット（部分一致）: {key}")
                return media_data
    
    return None
