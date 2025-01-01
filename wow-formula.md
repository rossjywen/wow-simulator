# 1. 屬性及效果

`主要屬性`有5個

- 力量(strenth)
- 敏捷(agility)
- 耐力(stamina)
- 智力(intellet)
- 精神(sprit)

---

`次要屬性`如下，分為物理相關、法系相關、都相關3類

**物理系相關的`次要屬性`**

- 攻擊強度(AP)
- 格擋(parry)
- 閃躲(dodge)
- 招架(block)
- 護甲穿透(armor penetration)

**法系相關的`次要屬性`**

- 法術強度(spell power)
- 法術穿透(spell pierce)

**都相關的`次要屬性`**

- 暴擊率(critical)
  - 法術暴擊
  - 物理暴擊
    - 遠程攻擊暴擊
    - 近戰攻擊暴擊
- 急速(haste)
- 命中(hit)

這些屬性有的會受到`主要屬性`的影響。一件裝備一般既提供`主要屬性`也提供`次要屬性`，所以最終到底提供了多少`次要屬性`需要計算得出(有個addon叫rating buster就是做這個工作的)。

關於物理攻擊的分類，物理攻擊分為兩種，一種是`近戰攻擊(melee attack)`的影響；一種是`遠程攻擊(ranged attack)`，不同的屬性作用於兩種攻擊有不同的加成公式。

## 1.1 主要屬性 

### 力量

力量 影響 戰士、DK、聖騎士、德魯伊

對於戰士、DK、聖騎士 

> 1點 力量 提升 2點 近戰攻擊AP
>
> 1點 力量 提升 0.27點招架

對於德魯伊

> 1點力量 提升 1點 近戰攻擊AP

### 敏捷

敏捷 影響 獵人、盜賊、戰士、德魯伊、薩滿

對於獵人

> 1點 敏捷 提升 2點 遠程攻擊AP
>
> 1點 敏捷 提升 1點 近戰攻擊AP
>
> 83點 敏捷 提升 百分之1暴擊率

對於戰士

> 1點 敏捷 提升 1點 遠程攻擊AP
>
> 1點 敏捷 提升 1點 近戰攻擊AP
>
> 62.4點 敏捷 提升 百分之1暴擊率

對於盜賊、德魯伊、薩滿

> 1點 敏捷 提升 1點 遠程攻擊AP
>
> 1點 敏捷 提升 2點 近戰攻擊AP
>
> 83點 敏捷 提升 百分之1暴擊率

實際上敏捷屬性對所有職業都提供暴擊增加，但是僅對上面的職業提供AP加成，所以真正使用敏捷的也就只有上面的職業最多，另外，我觀察到3.3.5有騎士也通過敏捷屬性來堆暴擊，僅提供暴擊，對於騎士來說 

>  每52點敏捷提供百分之1暴擊 無AP加成

另外，敏捷也提高閃躲(dodge)，這個就不考慮了，不影響傷害，pvp計算中我忽略閃躲招架等因素。

### 智力

智力會帶來3個效果

1. 魔法值
2. 法術暴擊

> 1點 智力 提升 20點 魔法值 (前20點例外 每點提供1點魔法值)
>
> 166.6 智力 提升 百分之1法術暴擊

#### 術士寶寶智力

術士寶寶隨著術士的智力 todo

### 精神

精神屬性最重要的功能就是回藍(mana regeneration)，`mana regeneration`分為兩個部分，`精神回藍(spirit mana regeneration)`和`戰鬥狀態回藍(combat mana regeneration)`。

精神回藍 把鼠標放在人物面板的base中的精神上面 就會顯示出來

戰鬥回藍  在戰鬥狀態下在人物面板的spell中

==其中，當處於非戰鬥狀態下，回藍是兩者的總和；而戰鬥狀態下僅能使用`戰鬥狀態回藍`==

==下面公式計算結果的單位是"每5秒回xxx"==

---

**精神回藍的公式**

對於牧師、德魯伊、薩滿、騎士 (也就是治療職業)

> $mana\_regen_{spirit} = 1.1287\times spirit$

對於法師

> $mana\_regen_{spirit} = 0.282175\times spirit$

*精神屬性對術士沒有任何效果*

---

**戰鬥回藍的公式**

> $mana\_regen_{combat} = 5\% \times class\_base\_mana$

上面公式中提到的"class_base_mana"也就是中文翻譯的"基礎法力值"，比如暗牧的第二層天賦"當..的時候，獲得百分之xx的基礎法力值"，這個"基礎法力值"是指80級人物==智力是0(不穿任何裝備也不點任何天賦)==的情況下的法力值，根據職業不同這個"基礎法力值"也不同，80級角色基礎法力值如下表。

| 職業   | 基礎法力值 |
| ------ | ---------- |
| 法師   | 3286       |
| 牧師   | 3863       |
| 德魯伊 | 3496       |
| 薩滿   | 4396       |
| 聖騎士 | 4394       |

另外，戰鬥回藍可以被天賦修改，典型的天賦如下

法師: 

​	奧術第4層 [arcane meditation] 

​	火焰倒數第5層 [pyromaniac] 

​	(這兩者還可疊加 因為都是增加 所以pvp火法要堆精神)

牧師: 

​	戒律第3層 [meditation]

### 耐力

todo

## 1.2 次要屬性

### 暴擊等級

從wlk 3.0.2開始，`暴擊等級`同時影響`近戰攻擊`、`遠程攻擊`、`魔法技能`，從暴擊等級到百分比的換算公式如下

> 45.91 暴擊等級 提升 百分之1 暴擊率

### 急速等級

`急速等級`同時影響`近戰攻擊`、`遠程攻擊`、`魔法技能`，在pvp中我沒見過有物理職業堆急速的，所以這裡先討論法系的急速效果。

**法術急速計算公式**

法術急速不會直接影響傷害值，但是會影響單位時間內的傷害值，對於80級，每32.79的急速等級提高1%的法術急速的公式如下。

> $Spell Haste = (SpellHaste Rating / 32.79)$
>
> $T_{NewCastTime} = T_{OldCastTime} / (1 + Spell Haste)$

---

**法術急速對GCD的影響**

法術急速公式不僅僅對於施法時間對於GCD同樣有效果，法系職業初始的GCD是1.5s。

所以就是把上面的公式帶入1.5計算就會得出最終被急速影響的GCD

---

**舉例對於一個冰法的寒冰箭加完天賦且擁有1000急速等級**

$T_{OldCastTime}=2.5s$

$Spell Haste = (1000 / 32.79) = 30.497\%$

$T_{NewCastTime} = 2.5 / (1 + 0.305) = 1.91s$

**GCD**

$T_{NewGCD}=1.5/(1+0.305)=1.15$

一個深度凍結5s 減去一個GCD等於3.85，大於1.91*2，==這就是為什麼PVP法師要達到1000急速的原因，要保證一個深度凍結能打出2根冰箭1根冰槍的效果。==

### 命中等級



### 躲閃 招架 格擋



## 1.3 最終效果

### 法術暴擊

**法術暴擊計算公式**

每種職業80級角色帶有恆定的`基礎法術暴擊率`，如下表(`DK`、`戰士`、`盜賊`不會從`智力`屬性收益到法術暴擊，因而他們也沒有職業自帶的恆定暴擊率)

| Class   | Class Constant |
| ------- | -------------- |
| Druid   | 1.85%          |
| Hunter  | 3.6%           |
| Mage    | 0.91%          |
| Paladin | 3.336%         |
| Priest  | 1.24%          |
| Shaman  | 2.2%           |
| Warlock | 1.701%         |

除了職業自帶先天屬性之外，影響暴擊的屬性有2個：`智力`和`暴擊等級`，對於80級

1. 每166.6667(也就是$\frac {500} {3}$)的智力值獲得百分之1的暴擊率提升；
2. 每45.91的暴擊等級獲得百分之1的暴擊率提升

所以最終的法術暴擊就是上面兩者的疊加

---

**法術暴擊bonus**

法術暴擊的bonus默認是50%的傷害，但是有一些天賦可以改變這個值，典型的就是法師的`碎冰`，這個天賦點滿的效果是暴擊的bonus翻倍，也就是一旦暴擊會提高100%的傷害。

---

**其他關於法術暴擊的信息**

1. 有些天賦的效果是"提高所有法術的法術暴擊"(如騎士懲戒系的`定罪`)；有些天賦的效果是"提高某一系法術的法術暴擊率"(如法師火焰系的`Critical Mass`)，這類天賦提高的暴擊率會顯示在人物面板上，==但是需要鼠標放在暴擊率那個地方，會顯示出不同的系的法術的暴擊，其中有的系比別的系高，但是總體的數值是不會改變的==。
2. 有些天賦的效果是"提高某一個或某幾個法術的法術暴擊率"(如法師火焰系的`incineration`)，這種天賦提高的暴擊率不會在面板上體現出來。
3. 鼠標移動到人物面板上的"智力"所顯示出來的log信息對應的就是公式的$ClassConstant+(Intellect/166.667)$ 部分(不包括裝備爆擊等級造成的提升)。

### 法術急速

急速僅受到`急速等級`的影響，詳見上文*急速等級*即可。

### 物理暴擊

分為`近戰暴擊率`和`遠程暴擊率`，受到`力量`、`敏捷`、`暴擊等級`的影響，==另外根據職業不同公式算法也不同，這些信息都在上文==。

# 2. 魔法技能計算公式

魔法技能的critical bonus默認是50%，也就是說默認法系技能暴擊得到1.5倍的傷害，這個數值會被天賦修改。

人物面板屬性影響法系技能傷害/治療的屬性為

1. 法術強度 spell power

2. 法術急速 spell haste

3. 法術暴擊 spell critic

## 2.1 法術強度和coefficient

**法術傷害總體公式**

> $Amount_{法術}= SpellBase+Coefficient\times SpellPower$

`SpellBase` 指的是技能說明中法術的基礎傷害

`Coefficient` 對於不同類型的法術有著不同的計算公式 見下面

---

**計算coefficient的特殊規則**

1. 下面使用的==$T_{PanelCastTime}$==指的是技能面板中初始狀態顯示的施法時間(==受天賦和裝備急速影響之前的施法時間==)
2. 直接(不包括引導型)法術施法時間==$T_{PanelCastTime}$大於7秒的按7秒計算==；==小於1.5秒的按1.5秒計算包括瞬發==；

### 直接傷害/治療 (direct)

**直接法術傷害公式：**

> $Coefficient = T_{PanelCast Time}/ 3.5 $

---

**直接法術治療量公式:**

> $Coefficient = (T_{PanelCastTime}/ 3.5) \times 1.88$

---

上面這兩個公式的意思是對於技能面板上不同的技能來說法術強度使其擁有的收益是不同的，施法時間越長的法術對法術強度的收益越大，大於7秒和小於1.5秒按照`規則1`來計算收益。

舉例來說法師的`火焰衝擊`

$T_{火焰衝擊} = 0$ (瞬發按照1.5計算)

$Coefficient = 1.5 / 3.5 = 42.86\%$

那麼火焰衝擊（不算任何天賦加成）的傷害就是 

$Amount_{火焰衝擊}= (925 – 1095) + SpellPower \times 42.86\%$

*其中"925-1095"是火焰衝擊的SpellBase*

### 非直接類傷害/治療 (dot/hot)

**dot傷害量計算公式:**

> $$Coefficient = T_{DotDuration} \quad / \quad 15$$

---

**hot治療量計算公式:**

> $$Coefficient = (T_{HotDuration} \quad / \quad 15) \times 1.88$$

---

舉例來說牧師的`暗言術:痛`持續時間18s，一共跳6次，那麼計算過程如下

$Coefficient_{暗言術:痛}=18/15=120\%$

每次跳傷害的加成

$Coefficient_{tick} = 120\%/6=20\%$

那麼`暗言術：痛`每次跳的傷害就是

$Amount_{tick}=1380/6 + 20\% \times SpellPowerc$

*其中1380是技能的SpellBase*

### 引導類傷害/治療 (channel)

計算公式和直接法術傷害相同，如果計算每一次傷害的量就除以次數即可。(==大於7秒的施法時間正常計算，不會強制鎖定到7秒==)

舉例法師的`奧術飛彈` 施法時間5s，一共跳5次，那麼計算過程如下

$Coefficient_{Total} = 5 / 3.5=142.86\%$

$Coefficient_{Tick} = Coefficient_{Total} / 5= 28.57\%$

### 直接和非直接混合型 (hybrid)

> $x = T_{DotDuration} / 15$
> $y = T_{CastTime} / 3.5$
> $Coefficient_{DoT} = x^2 / (x + y)$
> $Coefficient_{DD} = y^2 / (x + y)$
> $Coefficient_{Total} = Coefficient_{DoT} + Coefficient_{DD}$

---

Example calculation using the Rank 14 (L80) [Moonfire](https://wowwiki-archive.fandom.com/wiki/Moonfire) (Druid) spell:

```
Duration = 12.0 sec
Cast Time = instant (treated as 1.5 sec)

x = 12.0 / 15.0 = 0.8000
y = 1.5 / 3.5 = ~0.4286

CDot = 0.80002 / (0.8000 + 0.4286)
   = 0.6400 / 1.2286
   = 52.09%

CDD = 0.42862 / (0.8000 + 0.4286)
   = 0.1837 / 1.2286
   = 14.95%
```

### 群體技能 (aoe)

aoe技能必然是一個直接的(direct)法術，如牧師的`治療禱言`；或是一個引導的(channel)法術，如法師的`暴風雪`，絕不存在aoe技能是dot或hot。

無論是哪種aoe，都是按照direct的公式計算的前提下再乘以50%，公式如下。

**傷害法術:**

> $Coefficient = T_{PanelCastTime} / 3.5 \times 50\%$

---

**治療法術:**

> $Coefficient = (T_{PanelCastTime} / 3.5) \times 1.88 \times 50\%$

---

==從2.4版本引入一項修改使得一旦受到aoe傷害的目標大於一定數量就不會讓每一個個體都受到公式中的傷害；而是這些個體分擔某一個總和的傷害，這個公式wowwiki沒有給出。==

### 帶有特殊效果的技能 (effect)

比如寒冰箭這類除了傷害還帶有其他效果的技能在法術強度的收益上會乘以一個系數作為penalty，這個系數每個服務器實現的都不一樣，可能一些私服和官服的系數是不一樣的，Wowwiki給出的系數是95%。

這些特殊效果的技能可能是直接型的也可能是dot型的，總之都是在原有公式計算的基礎上再乘以一個系數。

==1. 計算effect必然是前麵包括direct dot/hot channel已經計算完之後再乘這個系數==

==2. 目前的技能並不存在hybrid且帶有effect的情況，direct帶有effect如法師的`寒冰箭`；dot帶有effect如德魯伊的`蟲群`。==

### 兼具傷害和治療的技能 

有一些技能的描述同時帶有傷害和治療的效果，這種技能典型的如
牧師的 `吞噬瘟疫` `神聖新星`
術士的 `吸取生命`
如`吸血鬼擁抱`這類buff造成的治療不算這類技能

這類技能wiki沒有給出絕對的公式，但是這類技能和hybrid技能一樣，符合`守恆定律`，所以可以得出下面的公式

> $Coefficient_{Damage} = Coefficient_{Total} \times \frac{傷害量} {傷害量+治療量}$
> $Coefficient_{Healing} = Coefficient_{Total} \times \frac{治療量} {傷害量+治療量}$

---

這類技能沒法通過公式計算，但是可以用這個公式來驗證測試出的結果。

下面列出wowwiki給出的分配比例，**用計算出的coefficient乘以這個比例就是真正的coefficient**。

| 技能                               | 分配比例     |
| ---------------------------------- | ------------ |
| 吞噬瘟疫(傷害)<br />吞噬瘟疫(治療) | 75%<br />25% |
| 吸取生命(傷害)<br />吸取生命(治療) | 50%<br />50% |
| 神聖新星(傷害)<br />神聖新星(治療) | 50%<br />50% |

==所以這類技能一定是帶有fixed標籤，並且我在模擬器中的做法是按照傷害和治療拆分成不同的技能。==

### 一些例外 (fixed)

說明這類技能的實際coefficient不是公式計算得來的，而是固定的猜測可能是固定設計或是被削弱過。

## 2.2 天賦的影響

**對於法術整體傷害/治療** (以百分比的形式做乘法)

1. 增加**所有**法術傷害/治療 (隱藏的，玩家無法直觀看到數值只能感受到效果)
2. 增加某一**系**法術傷害/治療 (隱藏的，玩家無法直觀看到數值只能感受到效果)
3. 增加某一**個**法術傷害/治療 (隱藏的，玩家無法直觀看到數值只能感受到效果)
4. 增加某一**個**法術的coefficient (隱藏的，玩家無法直觀看到數值只能感受到效果)

**對於法術暴擊率** (以百分比的形式做加法)

1. 增加**所有**法術的暴擊 (面板上能看到增加)
2. 增加某一**系**法術的暴擊 (==據說面板也能看到，需要確認==)
3. 增加某一**個**法術的暴擊 (隱藏的，玩家無法直觀看到數值只能感受到效果)

**對法術暴擊紅利** (以百分比的形式做乘法)

1. 增加**所有**法術的暴擊紅利
2. 增加**某一系**法術的暴擊紅利

**對於法術急速**

1. 增加**所有**法術的急速百分比 (面板上能看到增加)
2. 減少某一**個**法術的**面板施法時間** (==技能說明上能看到施法時間變化==)

## 2.3 技能屬性計算順序

所有**天賦**和**基礎屬性**最終都反應在一個技能的**內部屬性**上，而這些**內部屬性**最終決定了這個技能的所造成的效果的數值。這些屬性按照順序來計算，共分4個階段如下。

1. 技能的靜態數據 
   這部分信息來自沒有天賦和屬性作用效果時候的技能說明，初始的這部分數據完全是來自遊戲的設定信息，所以是完全靜態的。
2. 屬性
   因為這些值會被天賦使用到，包括`智力`、`精神`、`法術強度` 等。
3. 天賦對技能的影響 
   比如減少技能的施法時間，這個操作一定要在最終在法術急速的作用下計算實際施法時間==之前==就結算，否則就錯了。
4. 計算階段
   在上面的數據確定了之後就可以確定技能的屬性了，包括這些屬性包括`暴擊率`、`實際施法時間`等。

---

**一個技能在不同的階段確定的屬性**

| 階段         | 技能屬性                                                     |
| ------------ | ------------------------------------------------------------ |
| 技能靜態數據 | 1. 面板施法時間 (第一次計算)<br />2. coefficient (第一次計算) |
| 屬性         | 1. 法術強度 (最終結果)<br />2. 法術暴擊 (最終結果)<br />3. 法術急速 (最終結果) |
| 天賦         | 3. 實際面板施法時間(第二次計算，最終結果)<br />5. coefficient (第二次計算，最終結果)<br />6. (所有系/某一系/某一個) **技能數值**加成 (最終結果)<br />7. (某一系/某一個) **法術暴擊率**增加 (最終結果)<br />8. (所有系/某一系/某一個) **暴擊紅利**加成 (最終結果) |
| 計算階段     | 1. 這個法術的傷害加成<br />2. 這個法術的暴擊率<br />3. 這個法術的暴擊紅利<br />4. 這個法術的實際施法時間<br />5. GCD |

---

**法術最終數值加成**

> $Addition_{法術(最終)} = Addition_{所有法術} + Addition_{所在系} + Addition_{這個法術}$

---

**法術最終暴擊率**

> $Critical_{法術(最終)} = Class Constant + (Intellect / 166.6667) +  (Crit Rating / 45.91) + Critical_{所有法術增加} + Critical_{法術所屬系增加} + Critical_{這個法術增加} $

---

**法術最終暴擊紅利**

> $CriticalBonus_{法術(最終)}=CriticalBonus_{法術所屬系}+CriticalBonus_{這個法術}$

==$CriticalBonus_{所有系}$的初始值是0.5==

---

**法術實際施法時間**

> $T_{ActualCastTime} = T_{ModifiedPanelCastTime} / (1 + SpellHaste)$

---

**GCD**

> $GCD = 1.5 / (1 + SpellHaste)$

---

==模擬器中沒有單獨記錄"所有法術 提高xx"的記錄，而是直接加在了所有系上面，這樣更方便維護，詳見模擬器代碼。==

## 2.4 技能數值最終計算

### 直接法術(讀條)

**法術非暴擊數值計算**

> $Amount_{法術數值(非暴擊)min} = (SpellBase_{min} + SpellPower \times Coefficient)\times Addition_{法術(最終)}$
>
> $Amount_{法術數值(非暴擊)max} = (SpellBase_{max} + SpellPower \times Coefficient)\times Addition_{法術(最終)}$

---

**法術暴擊數值計算**

> $Amount_{法術數值(暴擊)min} = Amount_{法術數值(非暴擊)min} \times CriticalBonus_{法術(最終)}$
>
> $Amount_{法術數值(暴擊)max} = Amount_{法術數值(非暴擊)max} \times CriticalBonus_{法術(最終)}$

---

**法術平均數值計算**

> $Average_{min} = Amount_{法術數值(非暴擊)min} \times (1 - Critical_{法術(最終)}) + Amount_{法術數值(暴擊)min} \times Critical_{法術(最終)}$
>
> $Average_{max} = Amount_{法術數值(非暴擊)max} \times (1-Critical_{法術(最終)}) + Amount_{法術數值(暴擊)max} \times Critical_{法術(最終)}$

---

**法術單位時間數值計算**

> $DPS_{法術(非暴擊)min} = Amount_{法術數值(非暴擊)}/T_{ActualCastTime}$
>
> $DPS_{法術(非暴擊)max} = Amount_{法術數值(非暴擊)}/T_{ActualCastTime}$

---

### 直接法術(引導)

總體和上面相同，區別在於沒有min和max，同時引入了tick的概念。

### 時間性法術

> $Amount_{法術數值(總體)} = (SpellBase + SpellPower \times Coefficient)\times Addition_{法術(最終)}$
>
> $Amount_{法術數值(tick)} = Amount_{法術數值(總體)}/N_{tick}$

---

==WOW的設定dot是不能暴擊的，但是3.3.5引入了一些天賦使得dot也可以暴擊，如果點了這些天賦就可以把暴擊應用到dot的計算上。==

> $Amount_{法術數值(總體暴擊)} = Amount_{法術數值(總體)} \times CriticalBonus_{法術(最終)}$
>
> $Amount_{法術數值(tick暴擊)} = Amount_{法術數值(總體暴擊)}/N_{tick}$

---

### 混合型法術

上述兩部分都分析

# 3. 物理技能計算公式

武器技能的critical bonus默認是100%，也就是說默認武器技能暴擊得到2倍的傷害，這個數值會被天賦修改。

## 3.1 帶有武器傷害的技能

物理技能有不同的計算模型，我把不同的計算模型分為2種，一種是帶有`武器傷害`的計算模型，一種不帶，先說帶`武器傷害`的模型，`武器傷害`分為3種，如下。

- 武器傷害
  - 基礎武器傷害 base weapon damage
  - 被AP修改過的武器傷害
    - 非標準化的武器傷害 non-normalized attack-power-modified weapon damage
    - 標準化的武器傷害 normalized attack-power-modified weapon damage

---

`基礎武器傷害` 指的是武器的tooltips中展示的傷害範圍，*比如`穩固射擊`的說明中就提到的“未被修改的武器傷害”指的就是這個*



`非標準化的武器傷害` 指的是人物面板中物理頁面中的“近戰傷害”(==這裡注意一下，要把彈藥移除再看面板上的數值==)，這個值用作`自動射擊`、`自動攻擊`等，也叫`白字傷害`，因為自動攻擊在屏幕上的數字是白色的。公式如下 

> $weapon\_dmg_{non-norm} = base\_weapon\_dmg + (T * AP / 14)$

*T是武器的tooltip中的攻速*
*base_weapon_dmg是武器tooltip中的傷害範圍*

一些技能使用非標準化的武器傷害，如`奇美拉射擊`、`沈默射擊`，這類技能的tooltip都標注"百分之xx的武器傷害..."



`標準化的武器傷害` 其實和上面用的公式是相同的，區別是T不來自武器的tooltip，而是固定的，所以叫標準化，固定的數值根據不同的武器類型來決定，如下表

| 武器類型           | T    |
| ------------------ | ---- |
| 匕首               | 1.7  |
| 除匕首外的單手武器 | 2.4  |
| 雙手武器           | 3.3  |
| 遠程武器           | 2.8  |

==todo wowwiki中說"幾乎所有武器傷害技能都受到標準化的影響"，但我實際測試發現不是這樣，這個需要確認一下==

我測試的結果

驅散射擊這種 “百分之xxx 武器傷害” 都是 非標的 用的是武器實際速度作為系數

瞄准射擊 這種 “一次射擊” / 致死打死 "一次武器傷害" 都是 標的 用的是 標準化的速度作為系數

## 3.2 不帶有武器傷害的技能

除了上面的帶有"武器傷害"的計算公式之外，還有不受武器傷害影響的技能，這種技能最終的傷害只受到AP的影響，計算公式如下

> $ability\_dmg = base\_dmg + AP\times coefficient$

其中coefficient就是根據不同的技能有不同的系數了，通過查表即可得到。

舉例比如獵人的`毒蛇釘刺`，鼠標放在技能上顯示"xx秒造成xxx傷害"，最後的xxx傷害實際上就是已經受到了AP x cofficient之後加成的影響，所以當觸發增加AP的飾品buff的時候再把鼠標放在技能上發現這個數值改變了。

## 3.3 彈藥對遠程武器的傷害加成

遠程武器的`武器傷害`除了上面的部分外還有彈藥的影響，也就是說，==彈藥對遠程武器傷害的影響在計算武器傷害的階段就會計算==。

把鼠標停留在彈藥上會顯示"增加xxx傷害每秒"，所以根據不同的武器的攻擊速度，最終彈藥影響`武器傷害`的值是不同的，根據normalize和non-normalize的情況分為下面兩種。

---

**non-normalized 遠程武器傷害** 

易見到的就是`白字傷害`，實測我使用低級的箭[sharp arrow]-"add 3.5 DPS"，我使用弓[Fine Shortbow]-"10-20 speed 1.7"，實測面板數值提升白字傷害6點，計算如下

> dmg = 3.5 * 1.7 = 5.95

而當我使用284的弓，速度為3.0，實測面板數值提升了11點白字傷害，計算如下

> dmg = 3.5 * 3 = 10.5

---

**normalized 遠程武器傷害**

需要乘以的時間參數並不是武器的真實攻速，而是被normalize的時間，根據上面的公式可知，遠程武器normalize的時間是2.8，所以這個時間參數就是2.8.

> $dmg_{彈藥} = DPS_{彈藥} \times 2.8$

由於normalize計算武器傷害也是乘以2.8 所以相當於把tooltip中的"增加dps xxx點"中的xxx直接加上即可。

## 3.4 護甲穿透(ArP)

最開始我理解的護甲穿透就是按照面板上的tootip中的減少護甲的比例乘以目標的護甲，直到我使用了滿破的獵人測試發現不是這個情況，我才找到了護甲穿透真實的工作方法。

首先在80級版本，護甲穿透等級(Armor penetration rating)和tooltip中的比例換算的公式是

> $ ArP_{ratio} = ArP_{rating}/14$
>
> 每14點護甲穿透等級 = 1%的護甲減少

我找到的英文的資料如下

> Quote from: Ghostcrawler
>
> *Okay, here is a fairly technical explanation we put together for how armor pen works.*
>
> *We didn’t want Armor Penetration Rating to be too powerful against low armor targets, like it had been in BC. We also didn’t want Armor Penetration Rating to be too powerful against high armor targets.*

我猜測上面的信息是來自暴雪的設計人員的解釋，就是說在wlk中，他們設計的ArP希望運行的機制並不是對所有的人物都一樣，在TBC中ArP對於布甲表現的太過強勢；而同樣的也不想對護甲很高的角色殺傷力太高。

> *So, we decided on a system where there is a cap on how much armor the Armor Penetration Rating can be applied to. So, the first X armor on the target is reduced by the percentage listed in the Armor Penetration Rating tooltip, and all armor past that X is unaffected. Another way of understanding that is we multiply the percentage in the tooltip times the minimum of the two values: the cap, and the amount of armor on the target after all other modifiers.*

顯然這樣就需要設計一個數學公式來限制這個效果，在這個數學公式中，能計算出ArP減少護甲的比例能==作用到的==最多的護甲值，這個值稱之為cap，這個cap的存在能達到上面設計的思路和效果，這個公式如下

> cap = "(armor + C) / 3" 和 armor 兩者比較的最小的值
>
> armor是當前角色的護甲值，C是一個常數，根據目標等級計算得出，C的計算公式如下
>
> ```
> If (targetlevel < 60)
>    C = 400 + 85 * targetlevel
> Else
>    C = 400 + 85 * targetlevel + 4.5 * 85 * (targetlevel - 59);
> ```

在PVP中，玩家等級都是80，根據上面的公式，計算得出 C=15232.5，==這個值用在護甲減少物理傷害公式中==。

那麼舉個例子，一個牧師8000護甲，對於這個牧師來說

> armor = 8000
>
> (armor + C) / 3 = 7744
>
> cap是上面兩者中的較小的值 所以取7744

這個時候比如我的獵人滿破的能忽略100%護甲，這個"忽略100%護甲"的效果只能作用在這個牧師的7744的護甲上，所以忽略了7744 * 100% = 7744護甲，所以在這個獵人造成的物理傷害的過程中，這個牧師的護甲相當於是8000 - 7744 = 256.

從公式其實可以瞭解到，要想armor > (armor + C) / 3那麼護甲就要高於7616.5，==也就是說，在護甲值低於7616.5的情況下，ArP可以完全做用於護甲，一旦目標的護甲值高於7616.5就不可能完全忽略目標的護甲值==

# 4. 補充信息

## 4.1 護甲減少物理傷害

護甲分為幾個部分，`基礎護甲`(根據屬性自帶)、`裝備護甲`(裝備提供)、`魔法護甲`(法術提供 如法師[冰甲術])，所以總和如下公式

>  $armor_{all} = 2 \times Agility+ armor_{grear} + armor_{magic}$

護甲值提供對物理傷害的減傷效果，公式如下(僅提供80級pvp相關)

>  $Reduction = Armor / (Armor + 15232.5)$

15232.5這個數是怎麼來的 詳見 *護甲穿透(ArP)*

---

實測80級假人的物理減傷是百分之40，因為假人的減傷完全來自護甲，根據上面的公式可以帶入計算出，假人的

> 0.4 = X / X + 15232.5
>
> 2X + 15232.5 * 2 = 5X
>
> 所以 X = 10155

最後計算出結果，80級假人的護甲是10155，減傷效果是40%。

## 4.2 pvp韌性減傷

用我的術士打我的法師1372韌性(所有傷害降低29.11% 被暴擊率降低14.55% 暴擊傷害32.02%)

實測獻祭 直接部分 非暴擊1101 / 獻祭正常非暴擊1553 = 70.895% 符合上面降低所有傷害的結果

實測獻祭 直接部分 暴擊1496 / 獻祭正常暴擊1552 * 2 = 3104 = 48.195% 這個也符合上面的 如下

> (1-0.2911) * (1 - 0.3202) = 0.481484

1564

## 4.3 技能減傷



## 4.4 增加暴擊傷害寶石效果



# 5. 代碼實現

代碼結構如下

- attribute.py 實現了對技能有影響的屬性數據
  - class Attribute 屬性
- ability.py 實現了技能相關代碼 包括技能靜態和計算公式
  - class Spell_ability 魔法技能
  - class Physic_ability 物理技能 其中包含近戰和遠程物理技能
- mage.py/warlock.py/priest.py.... 實現各個職業天賦對技能的影響
- sim.py 實現模擬器的運行 運行 python3 sim.py --help 可查看幫助

## 5.1 人物屬性

人物屬性的角度，法系技能傷害和`spell power` `haste` `critical`這幾點相關；除此之外還和技能本身的tooltip中提供的傷害相關，兩者是疊加關係，所以計算法系傷害之前需要讀取==人物面板的屬性==。

但是問題來了，人物面板的屬性有可能受到天賦的影響，由上文可知有一些天賦影響面板的數值；有一些影響看不到數值只能感受到效果，所以我寫模擬器的時候就需要做出選擇，"到底是盡量依賴遊戲的算法還是盡量自己來通過raw data來計算出這些屬性?"，最後我決定還是==盡量依賴遊戲的算法==，這樣做的好處是減少我自己算錯的風險。

模擬器需要模擬天賦對技能的影響，所以我的做法就是

1. 實現天賦的模擬的時候==影響面板數值的天賦都忽略==
2. 直接去拿一個角色==穿好裝備且點好天賦==的面板數據

## 5.2 技能分類

另一方面就是技能的分類，上文已經說明瞭技能的分類，我把這些分類做成了tag，因為這些分類會進行排列組合。在一個csv文件中記錄著每個職業法系技能的tag和傷害、基礎施法時間等信息，這些信息如下。

- `ability_name` 技能名稱
- `ability_type` 技能類型 magic/physical
- `ability_attribute_tags` 技能具備的性質的tag 下文具體說tag的信息
- `panel_cast_time` 未被天賦和急速修改過的施法時間
- `direct_property` 直接的傷害/治療 數值
  - 直接法術 x-y 其中x是傷害的最小值 y是傷害的最大值 表示一個範圍
  - 引導法術 x-y 其中x是傷害總和 y是tick數
- `periodic_property` 週期性的傷害/治療 數值
  - x-y-z 其中x是傷害總和 y是持續時間 z是tick數
- `school` 技能傷害所屬系(僅對魔法技能有用 6個系 冰霜、火焰、奧術、神聖、暗影、自然)
- `database_coefficient` 網站wow-wiki給出的測試出的系數
- `label` 這些法術在指定哪些label的情況下需要測試 (比如冰法就不需要測試 [龍吸術]了) 

在這些中，`spell_attribute_tags`還需要再具體分類，法系技能的tag如下表。

| tag name | explanation                         |
| -------- | ----------------------------------- |
| dmg      | 傷害性法術                          |
| heal     | 治療法術                            |
| absorb   | 吸收傷害法術                        |
| direct   | 直接性法術                          |
| channel  | 引導型法術                          |
| dot/hot  | 週期性法術                          |
| hybrid   | 具有"直接"和"週期性"的效果          |
| aoe      | aoe型法術                           |
| fixed    | 系數不能使用公式計算 而是一個固定值 |
| effect   | 帶有特殊效果 比如 減速 等           |

這些標籤對計算公式的影響見上文和代碼

物理技能的tag如下表 todo



## 5.3 class Attribute

這個類除了需要的面板屬性之外還記錄"全局的技能變化"，也就是對某個系或整體所有法術的屬性的變化

---

`spell_basic_attr` 字典，包含上文提到的基本數據，包含`spell power` `haste` `critical`這幾個數據

---

`spell_critical_increase` 字典，包含不同系法術的法術增加的暴擊值，如法師[深冬之寒]增加冰系法術的暴擊率

(只有天賦會改變這個變量，且不會顯示在面板上)

---

`spell_amount_increase` 字典，包含不同系法術的傷害增加值，如法師[刺骨寒冰]

這個會影響技能的tooltip，所以模擬器讀取的靜態技能數據都是點天賦之前的tooltip。



## 5.4 class Ability

## 5.5 模擬天賦對技能的修改

**全局**：

1. 增加所有傷害
   		遍歷所有.nature是'dmg'的技能 然後增加.specific_amount_increase
2. 增加所有治療
   		遍歷所有.nature是'heal'的技能 然後增加.specific_amount_increase

**法系傷害**：

1. 增加某一個技能傷害
   		增加這個技能的.specific_amount_increase
2. 增加某一個系技能傷害
   		增加self.spell_amount_increase['所屬school']
3. 增加所有法術傷害
   		遍曆法術技能 增加.specific_amount_increase

**法系治療**：

1. 增加某一個技能治療
   		增加這個技能的.specific_amount_increase

**物理**：

	1. 增加某一個技能傷害
		增加這個技能的.specific_amount_increase
	1. 增加近戰傷害
	遍歷找到所有.ability_type == 'melee'的技能 增加.specific_amount_increase
	1. 增加遠程傷害
	遍歷找到所有.ability_type == 'ranged'的技能 增加.specific_amount_increase
	1. 增加某一種傷害
	遍歷找到所有.school == 某一種類型的技能 增加.specific_amount_increase

# 6. 代碼命令及附帶工具

## 測試各職業的命令

**法師**

冰法pvp

> python3 sim.py --class=mage --talent=talent_data/mage_frost_pvp.json --attribute=attribute_data/mage_s8_frost.csv

火法pvp

> python3 sim.py --class=mage --talent=talent_data/mage_fire_pvp.json --attribute=attribute_data/mage_s8_fire.csv

---

**牧師**

暗牧pvp

> python3 sim.py --class=priest --talent=talent_data/priest_shadow_2v2.json --attribute=attribute_data/priest_s8_shadow.csv

戒律pvp (急速)

> python3 sim.py --class=priest --talent=talent_data/priest_disc_solo.json --attribute=attribute_data/priest_s8_disc_haste.csv

---

**術士**

毀滅術pvp

> python3 sim.py --class=warlock --talent=talent_data/warlock_destruction_pvp.json --attribute=attribute_data/warlock_s8.csv

痛苦術pvp

> python3 sim.py --class=warlock --talent=talent_data/warlock_affliction_pvp.json --attribute=attribute_data/warlock_s8.csv

---

**獵人**

射擊獵人(100%破甲的T10.75)

> python3 sim.py --class=hunter --talent=talent_data/hunter_mm_pvp.json --attribute=attribute_data/hunter_T10_mm.csv

射擊獵人(s8)

> python3 sim.py --class=hunter --talent=talent_data/hunter_mm_pvp.json  --attribute=attribute_data/hunter_s8.csv

---

**DK**

> python3 sim.py --class=DK --talent=talent_data/DK_unholy_pvp.json --attribute=attribute_data/DK_s8.csv

---

**聖騎士**

奶騎

> python3 sim.py --class=paladin --talent=talent_data/paladin_holy_pvp.json  --attribute=attribute_data/paladin_s8_holy.csv

---

**盜賊**

敏銳(穿pvp散裝)

> python3 sim.py --class=rogue --talent=talent_data/rogue_subtlety_pvp.json --attribute=attribute_data/rogue_s8_pvp.csv

敏銳(穿pve散裝)

> python3 sim.py --class=rogue --talent=talent_data/rogue_subtlety_pvp.json --attribute=attribute_data/rogue_s8_pve.csv

刺殺(穿pvp散裝)

> python3 sim.py --class=rogue --talent=talent_data/rogue_assassination_pvp.json --attribute=attribute_data/rogue_s8_pvp.csv

---

**戰士**

武器戰

> 

## excel天賦dump成json的命令

> ./dump_from_excel.py --input=WOW-talents.xlsx --page=no-talent --start=a2 --end=l12 --type=list > no_talent.json

