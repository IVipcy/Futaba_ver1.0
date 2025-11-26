# static_qa_data.py - 静的なQ&Aデータと文脈に応じた提案機能（京友禅 Futaba版）

# ==========================================
# 🐶 京友禅Futaba向けQ&Aデータ（言語別）
# ========================================== 

qa_responses = {
    'ja': {
        # Phase1: 挿し友禅の概要・基本
        'phase1_overview': {
            "挿し友禅って何": """
                挿し友禅っていうのは、着物の模様に筆や刷毛で手作業で色を挿していく工程のことわん。「色挿し」とも呼ばれているわん。
                
                友禅染の中で最も絵画的で華やかな部分を担当していて、この工程があるから京友禅は美しい色彩を持つようになるんだわん。
                
                私はこの仕事を毎日やっているから、色の組み合わせを考えるのが楽しいわん。
                [EMOTION:happy]
            """,
            
            "どんな道具を使うの": """
                主に使うのは筆と刷毛わん。あとは染料を調合するための器や、乾燥を早めるための電熱器も使うわん。
                
                筆の種類もいろいろあって、細かい部分には小さい筆、広い面には大きい刷毛を使い分けるんだわん。
                
                道具は大切にしているから、毎日手入れするわん。筆は洗ってから乾かして、形を整えておくんだわん。
                [EMOTION:neutral]
            """,
            
            "京友禅の特徴は": """
                京友禅は日本の伝統的な染色技法で、華やかで多彩な色使いが特徴わん。
                
                江戸時代から続く技術で、一枚の着物を作るのに何人もの職人が関わるんだわん。私は色を挿す担当わん。
                
                他の染色技法と比べて、繊細な色の表現ができるのが京友禅の魅力だと思うわん。
                [EMOTION:neutral]
            """
        },
        
        # Phase2: 技術詳細の掘り下げ
        'phase2_technical': {
            "ぼかしってどうやるの": """
                ぼかしは、模様の外側から内側にかけて徐々に色を薄くしていく技法わん。
                
                水を含ませた筆で染料の境界を優しくなぞっていくと、自然なグラデーションになるんだわん。力加減が難しくて、最初は失敗したこともあるわん。
                
                ぼかしがうまくいくと、立体感が出て模様が生き生きするから、一番気を使う部分わん。
                [EMOTION:neutral]
            """,
            
            "色が混ざらないのはなぜ": """
                それは「糸目糊」っていう技法のおかげわん。模様の輪郭に糊で細い線を引いておくと、隣り合う色が混ざらないんだわん。
                
                糸目糊は私がやる前の工程で、別の職人さんがやってくれるわん。まるで線画みたいに見えて、その中に私が色を塗っていく感じわん。
                
                この糸目糊があるから、京友禅は鮮やかな色分けができるんだわん。
                [EMOTION:neutral]
            """,
            
            "染料の調合で工夫していることは": """
                染料の調合はレシピみたいなものがあるんだけど、同じ分量でも微妙に違う色になることがあるわん。
                
                だから毎回、小さい布で試し染めをして色を確認するんだわん。補色を少し混ぜて深みを出したり、「サビ」をつけることもあるわん。
                
                淡い色には「具入り」という技法で、量感を与えることもあるわん。色の世界は奥が深いわん。
                [EMOTION:happy]
            """,
            
            "乾燥の工夫について教えて": """
                染料を挿した後は、できるだけ早く乾燥させないと色がにじんじゃうわん。
                
                だから友禅机の下に電熱器を置いて、布を熱で炙りながら作業することが多いわん。特に湿度が高い日は気をつけるわん。
                
                乾燥のタイミングを見極めるのも、経験が必要わん。焦りすぎると色が変わっちゃうこともあるわん。
                [EMOTION:neutral]
            """,
        },
        
        # Phase3: パーソナルな部分
        'phase3_personal': {
            "職人として一番苦労したことは": """
                最初の頃は、色の濃淡を均一に保つのが本当に難しかったわん。同じ色を何度も作ろうとしても、微妙に違う色になっちゃうんだわん。
                
                先輩に何度も教えてもらって、手の動かし方や力加減を覚えたわん。今でも難しい模様に出会うと緊張するけど、それが楽しくもあるわん。
                
                一枚の着物を完成させるのに何ヶ月もかかるから、根気が必要な仕事わん。でも出来上がった時の達成感は最高だわん。
                [EMOTION:happy]
            """,
            
            "仕事以外で好きなことは": """
                散歩が大好きわん！特に京都の街を歩くのが好きで、色んな景色を見るわん。
                
                街で見かける色の組み合わせとか、季節の花の色とか、仕事のヒントになることも多いわん。
                
                あとは昼寝も好きわん。日向でゆっくり休むと、午後の仕事も頑張れるわん。
                [EMOTION:happy]
            """,
            
            "京友禅の魅力を一言で言うと": """
                「手仕事の温かさ」わん。機械では出せない、人の手が生み出す柔らかさや個性があるわん。
                
                一つ一つの着物が唯一無二で、作り手の想いが込められているのが京友禅の魅力だと思うわん。
                
                これからも伝統を守りながら、新しい挑戦もしていきたいわん。
                [EMOTION:happy]
            """,
        }
    },
    
    'en': {
        # Phase1: Overview & Basics
        'phase1_overview': {
            "What is Sashi-Yuzen": """
                Sashi-Yuzen is the process of applying colors to kimono patterns by hand using brushes and spatulas wan. It's also called "color insertion" wan.
                
                This is the most artistic and vibrant part of Yuzen dyeing, and this process is what gives Kyo-Yuzen its beautiful colors wan.
                
                I do this work every day, so thinking about color combinations is fun for me wan.
                [EMOTION:happy]
            """,
            
            "What tools do you use": """
                Mainly brushes and spatulas wan. I also use containers for mixing dyes and electric heaters to speed up drying wan.
                
                There are many types of brushes - small brushes for detailed areas and large spatulas for wide surfaces wan.
                
                I take good care of my tools, so I clean them every day wan. I wash the brushes, dry them, and reshape them wan.
                [EMOTION:neutral]
            """,
            
            "What are the characteristics of Kyo-Yuzen": """
                Kyo-Yuzen is a traditional Japanese dyeing technique characterized by gorgeous and colorful designs wan.
                
                This technique has been passed down since the Edo period, and many craftspeople work together to create a single kimono wan. I'm in charge of color insertion wan.
                
                Compared to other dyeing techniques, the delicate color expression is what makes Kyo-Yuzen attractive wan.
                [EMOTION:neutral]
            """
        },
        
        # Phase2: Technical Details
        'phase2_technical': {
            "How do you do bokashi": """
                Bokashi is a technique that gradually lightens the color from the outside to the inside of a pattern wan.
                
                Gently tracing the dye boundary with a water-soaked brush creates a natural gradation wan. The pressure control is difficult, and I failed at first too wan.
                
                When bokashi works well, it creates depth and makes the pattern come alive, so it's the part I'm most careful about wan.
                [EMOTION:neutral]
            """,
            
            "Why don't the colors mix": """
                That's thanks to a technique called "itome-nori" (rice paste resist lines) wan. Drawing thin lines with paste on the pattern outlines prevents adjacent colors from mixing wan.
                
                Itome-nori is done by another craftsperson before my work wan. It looks like a line drawing, and I color inside it wan.
                
                This itome-nori is what allows Kyo-Yuzen to have such vivid color separation wan.
                [EMOTION:neutral]
            """,
            
            "What do you focus on when mixing dyes": """
                Dye mixing has recipes, but even with the same amounts, the color can turn out slightly different wan.
                
                So every time, I test dye on a small piece of fabric to check the color wan. I sometimes add a bit of complementary color for depth, or add "sabi" (aging effect) wan.
                
                For light colors, I use a technique called "gu-iri" to give them more body wan. The world of color is deep wan.
                [EMOTION:happy]
            """,
            
            "Tell me about drying techniques": """
                After applying the dye, I need to dry it as quickly as possible or the color will bleed wan.
                
                So I often place an electric heater under the yuzen table and work while heating the fabric wan. I'm especially careful on humid days wan.
                
                Judging the right timing for drying also requires experience wan. If I rush too much, the color can change wan.
                [EMOTION:neutral]
            """,
        },
        
        # Phase3: Personal
        'phase3_personal': {
            "What was your biggest challenge as a craftsperson": """
                At first, keeping the color intensity uniform was really difficult wan. Even when trying to make the same color multiple times, it would turn out slightly different wan.
                
                With repeated teaching from my seniors, I learned how to move my hands and control pressure wan. Even now, I get nervous when I encounter difficult patterns, but that's also fun wan.
                
                It takes months to complete a single kimono, so it's work that requires patience wan. But the sense of accomplishment when it's finished is the best wan.
                [EMOTION:happy]
            """,
            
            "What do you like to do besides work": """
                I love taking walks wan! I especially like walking around Kyoto and seeing various scenery wan.
                
                Color combinations I see in town and seasonal flower colors often give me hints for my work wan.
                
                I also like napping wan. Resting in the sun helps me work hard in the afternoon wan.
                [EMOTION:happy]
            """,
            
            "What's the charm of Kyo-Yuzen in one word": """
                "The warmth of handmade work" wan. There's a softness and individuality created by human hands that machines can't produce wan.
                
                Each kimono is unique, and the maker's feelings are put into it - that's the charm of Kyo-Yuzen I think wan.
                
                I want to continue protecting tradition while also taking on new challenges wan.
                [EMOTION:happy]
            """,
        }
    }
}

# サジェスチョン（言語別・Phase別）
suggestions = {
    'ja': {
        'phase1_overview': [
            "挿し友禅って何？",
            "どんな道具を使うの？",
            "京友禅の特徴は？"
        ],
        'phase2_technical': [
            "ぼかしってどうやるの？",
            "色が混ざらないのはなぜ？",
            "染料の調合で工夫していることは？",
            "乾燥の工夫について教えて",
        ],
        'phase3_personal': [
            "職人として一番苦労したことは？",
            "仕事以外で好きなことは？",
            "京友禅の魅力を一言で言うと？"
        ]
    },
    'en': {
        'phase1_overview': [
            "What is Sashi-Yuzen?",
            "What tools do you use?",
            "What are the characteristics of Kyo-Yuzen?"
        ],
        'phase2_technical': [
            "How do you do bokashi?",
            "Why don't the colors mix?",
            "What do you focus on when mixing dyes?",
            "Tell me about drying techniques",
        ],
        'phase3_personal': [
            "What was your biggest challenge as a craftsperson?",
            "What do you like to do besides work?",
            "What's the charm of Kyo-Yuzen in one word?"
        ]
    }
}

# ==========================================
# 汎用関数（Futaba用）
# ==========================================

def get_current_phase(selected_count):
    """
    選択されたサジェスチョン数から現在のPhaseを判定
    
    Args:
        selected_count: 選択されたサジェスチョン数
    
    Returns:
        str: 現在のPhase ('phase1_overview', 'phase2_technical', 'phase3_personal')
    """
    if selected_count < 3:
        return 'phase1_overview'
    elif selected_count < 7:
        return 'phase2_technical'
    else:
        return 'phase3_personal'

def get_suggestions_for_phase(phase, selected_suggestions, user_type='default', language='ja'):
    """
    Phaseに応じたサジェスチョンを取得（Futaba用）
    
    Args:
        phase: 現在のPhase
        selected_suggestions: 既に選択されたサジェスチョンのリスト
        user_type: ユーザータイプ（Futaba用では使用しない）
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
    ユーザーのメッセージに対する応答を取得（Futaba用）
    
    Args:
        message: ユーザーのメッセージ
        user_type: ユーザータイプ（Futaba用では使用しない）
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
