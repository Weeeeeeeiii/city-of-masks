# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define lin = Character("林岚")
define li = Character("黎弦")
define mm = Character("神秘男子")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg city of masks
    with fade

    "你是女主角「林岚」，一位刚进入镜界都市的新记者，收到匿名线报，称有“身份消失”的案件不断在午夜发生。"

    "你来到这座城市，意外得知自己也在午夜被赋予了一个面具和第二人格。"

    "调查的过程中，你遇见了四位关键男性角色，每人都隐藏着一段关于镜界的秘密。"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

label bell_tower:
    scene bg bell tower
    with fade

    "傍晚，城市钟楼下，阳光渐沉，一封匿名信被悄悄塞进你住处的门缝。"

    "信上写着：\n“午夜后，城市才睁开眼睛。来钟楼，找回真正的自己。”"

    "你略感不安，却又被莫名的好奇牵引着走出门去。钟声敲响，世界一瞬间褪色——你站在镜界中的钟楼广场上，四周人群戴着各异的面具。"

    show lixian mask

    mm "你终于来了，林岚。欢迎来到真实的镜界。你，还记得你是谁吗？"

    menu:

        "你是谁？为什么知道我的名字？":
            jump smile_of_guide

        "我当然知道我是谁，但你似乎搞错了。":
            jump another_me


label smile_of_guide:
    scene bg bell tower
    with fade

    show lixian mask handup

    mm "啊……果然你还是不记得我了。也对，你刚踏入这里，意识还没稳定。"

    show lixian mask

    "他停顿片刻，从西装内袋取出一张泛黄的旧报纸，递给你。"

    "报纸头条" "年轻记者林岚，神秘失踪已三日。\n……"

    "你愣住了——这份报纸的日期是三天前。你却清楚记得，自己是在今天才抵达这座城市。"

    mm "在镜界，没有人只来一次。你曾来过，也曾……失去自己。"

    show lixian

    "他摘下面具——你惊讶地发现他与白天在新闻中心擦肩而过的一位陌生男子长得一模一样。"

    mm "我叫“黎弦”，是你的引路人。也是……你的前搭档。"

    "你大脑开始发胀，某些片段模糊地闪现，但无法看清。你开始怀疑自己到底遗忘了什么。"

label another_me:
    scene bg bell tower
    with fade

    show lixian mask

    "面具下的男人微微一愣，仿佛被你反将一军。"

    "但下一秒，他却轻笑出声，低沉的声音中带着一丝兴奋："

    mm "果然……你是“现在的你”。"

    "他轻轻拍了两下手，像是对你的反应感到满意，又像是在某种实验中验证了假设。"

    mm "在镜界，“你是谁”并不是你说了算。"

    "他抬起一只手，做了个轻点你眉心的动作。"

    scene double linlan

    "一道奇异的光在你面前一闪，四周的场景仿佛碎裂的镜面一般抖动了一瞬。"

    "一个长相与你一模一样的女孩，穿着你没有见过的黑衣，站在黑暗的镜中世界，冷冷地凝视着你。"

    "镜中女孩" "你来晚了。"

    "你感到一阵强烈的撕裂感，脑海中似乎有另一个你在挣扎着想要“上来”。"