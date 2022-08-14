# 1. 属性及效果

`主要属性`有5个

- 力量(strenth)
- 敏捷(agility)
- 耐力(stamina)
- 智力(intellet)
- 精神(sprit)

---

`次要属性`如下，分为物理相关、法系相关、都相关3类

**物理系相关的`次要属性`**

- 攻击强度(AP)
- 格挡(parry)
- 闪躲(dodge)
- 招架(block)
- 护甲穿透(armor penetration)

**法系相关的`次要属性`**

- 法术强度(spell power)
- 法术穿透(spell pierce)

**都相关的`次要属性`**

- 暴击率(critical)
  - 法术暴击
  - 物理暴击
    - 远程攻击暴击
    - 近战攻击暴击
- 急速(haste)
- 命中(hit)

这些属性有的会受到`主要属性`的影响。一件装备一般既提供`主要属性`也提供`次要属性`，所以最终到底提供了多少`次要属性`需要计算得出(有个addon叫rating buster就是做这个工作的)。

关于物理攻击的分类，物理攻击分为两种，一种是`近战攻击(melee attack)`的影响；一种是`远程攻击(ranged attack)`，不同的属性作用于两种攻击有不同的加成公式。

## 1.1 主要属性 

### 力量

力量 影响 战士、DK、圣骑士、德鲁伊

对于战士、DK、圣骑士 

> 1点 力量 提升 2点 近战攻击AP
>
> 1点 力量 提升 0.27点招架

对于德鲁伊

> 1点力量 提升 1点 近战攻击AP

### 敏捷

敏捷 影响 猎人、盗贼、战士、德鲁伊、萨满

对于猎人

> 1点 敏捷 提升 2点 远程攻击AP
>
> 1点 敏捷 提升 1点 近战攻击AP
>
> 83点 敏捷 提升 百分之1暴击率

对于战士

> 1点 敏捷 提升 1点 远程攻击AP
>
> 1点 敏捷 提升 1点 近战攻击AP
>
> 62.4点 敏捷 提升 百分之1暴击率

对于盗贼、德鲁伊、萨满

> 1点 敏捷 提升 1点 远程攻击AP
>
> 1点 敏捷 提升 2点 近战攻击AP
>
> 83点 敏捷 提升 百分之1暴击率

实际上敏捷属性对所有职业都提供暴击增加，但是仅对上面的职业提供AP加成，所以真正使用敏捷的也就只有上面的职业最多，另外，我观察到3.3.5有骑士也通过敏捷属性来堆暴击，仅提供暴击，对于骑士来说 

>  每52点敏捷提供百分之1暴击 无AP加成

另外，敏捷也提高闪躲(dodge)，这个就不考虑了，不影响伤害，pvp计算中我忽略闪躲招架等因素。

### 智力

智力会带来3个效果

1. 魔法值
2. 法术暴击

> 1点 智力 提升 20点 魔法值 (前20点例外 每点提供1点魔法值)
>
> 166.6 智力 提升 百分之1法术暴击

#### 术士宝宝智力

术士宝宝随着术士的智力 todo

### 精神

精神属性最重要的功能就是回蓝(mana regeneration)，`mana regeneration`分为两个部分，`精神回蓝(spirit mana regeneration)`和`战斗状态回蓝(combat mana regeneration)`。

精神回蓝 把鼠标放在人物面板的base中的精神上面 就会显示出来

战斗回蓝  在战斗状态下在人物面板的spell中

==其中，当处于非战斗状态下，回蓝是两者的总和；而战斗状态下仅能使用`战斗状态回蓝`==

==下面公式计算结果的单位是"每5秒回xxx"==

---

**精神回蓝的公式**

对于牧师、德鲁伊、萨满、骑士 (也就是治疗职业)

> $mana\_regen_{spirit} = 1.1287\times spirit$

对于法师

> $mana\_regen_{spirit} = 0.282175\times spirit$

*精神属性对术士没有任何效果*

---

**战斗回蓝的公式**

> $mana\_regen_{combat} = 5\% \times class\_base\_mana$

上面公式中提到的"class_base_mana"也就是中文翻译的"基础法力值"，比如暗牧的第二层天赋"当..的时候，获得百分之xx的基础法力值"，这个"基础法力值"是指80级人物==智力是0(不穿任何装备也不点任何天赋)==的情况下的法力值，根据职业不同这个"基础法力值"也不同，80级角色基础法力值如下表。

| 职业   | 基础法力值 |
| ------ | ---------- |
| 法师   | 3286       |
| 牧师   | 3863       |
| 德鲁伊 | 3496       |
| 萨满   | 4396       |
| 圣骑士 | 4394       |

另外，战斗回蓝可以被天赋修改，典型的天赋如下

法师: 

​	奥术第4层 [arcane meditation] 

​	火焰倒数第5层 [pyromaniac] 

​	(这两者还可叠加 因为都是增加 所以pvp火法要堆精神)

牧师: 

​	戒律第3层 [meditation]

### 耐力

todo

## 1.2 次要属性

### 暴击等级

从wlk 3.0.2开始，`暴击等级`同时影响`近战攻击`、`远程攻击`、`魔法技能`，从暴击等级到百分比的换算公式如下

> 45.91 暴击等级 提升 百分之1 暴击率

### 急速等级

`急速等级`同时影响`近战攻击`、`远程攻击`、`魔法技能`，在pvp中我没见过有物理职业堆急速的，所以这里先讨论法系的急速效果。

**法术急速计算公式**

法术急速不会直接影响伤害值，但是会影响单位时间内的伤害值，对于80级，每32.79的急速等级提高1%的法术急速的公式如下。

> $Spell Haste = (SpellHaste Rating / 32.79)$
>
> $T_{NewCastTime} = T_{OldCastTime} / (1 + Spell Haste)$

---

**法术急速对GCD的影响**

法术急速公式不仅仅对于施法时间对于GCD同样有效果，法系职业初始的GCD是1.5s。

所以就是把上面的公式带入1.5计算就会得出最终被急速影响的GCD

---

**举例对于一个冰法的寒冰箭加完天赋且拥有1000急速等级**

$T_{OldCastTime}=2.5s$

$Spell Haste = (1000 / 32.79) = 30.497\%$

$T_{NewCastTime} = 2.5 / (1 + 0.305) = 1.91s$

**GCD**

$T_{NewGCD}=1.5/(1+0.305)=1.15$

一个深度冻结5s 减去一个GCD等于3.85，大于1.91*2，==这就是为什么PVP法师要达到1000急速的原因，要保证一个深度冻结能打出2根冰箭1根冰枪的效果。==

### 命中等级



### 躲闪 招架 格挡



## 1.3 最终效果

### 法术暴击

**法术暴击计算公式**

每种职业80级角色带有恒定的`基础法术暴击率`，如下表(`DK`、`战士`、`盗贼`不会从`智力`属性收益到法术暴击，因而他们也没有职业自带的恒定暴击率)

| Class   | Class Constant |
| ------- | -------------- |
| Druid   | 1.85%          |
| Hunter  | 3.6%           |
| Mage    | 0.91%          |
| Paladin | 3.336%         |
| Priest  | 1.24%          |
| Shaman  | 2.2%           |
| Warlock | 1.701%         |

除了职业自带先天属性之外，影响暴击的属性有2个：`智力`和`暴击等级`，对于80级

1. 每166.6667(也就是$\frac {500} {3}$)的智力值获得百分之1的暴击率提升；
2. 每45.91的暴击等级获得百分之1的暴击率提升

所以最终的法术暴击就是上面两者的叠加

---

**法术暴击bonus**

法术暴击的bonus默认是50%的伤害，但是有一些天赋可以改变这个值，典型的就是法师的`碎冰`，这个天赋点满的效果是暴击的bonus翻倍，也就是一旦暴击会提高100%的伤害。

---

**其他关于法术暴击的信息**

1. 有些天赋的效果是"提高所有法术的法术暴击"(如骑士惩戒系的`定罪`)；有些天赋的效果是"提高某一系法术的法术暴击率"(如法师火焰系的`Critical Mass`)，这类天赋提高的暴击率会显示在人物面板上，==但是需要鼠标放在暴击率那个地方，会显示出不同的系的法术的暴击，其中有的系比别的系高，但是总体的数值是不会改变的==。
2. 有些天赋的效果是"提高某一个或某几个法术的法术暴击率"(如法师火焰系的`incineration`)，这种天赋提高的暴击率不会在面板上体现出来。
3. 鼠标移动到人物面板上的"智力"所显示出来的log信息对应的就是公式的$ClassConstant+(Intellect/166.667)$ 部分(不包括装备爆击等级造成的提升)。

### 法术急速

急速仅受到`急速等级`的影响，详见上文*急速等级*即可。

### 物理暴击

分为`近战暴击率`和`远程暴击率`，受到`力量`、`敏捷`、`暴击等级`的影响，==另外根据职业不同公式算法也不同，这些信息都在上文==。

# 2. 魔法技能计算公式

魔法技能的critical bonus默认是50%，也就是说默认法系技能暴击得到1.5倍的伤害，这个数值会被天赋修改。

人物面板属性影响法系技能伤害/治疗的属性为

1. 法术强度 spell power

2. 法术急速 spell haste

3. 法术暴击 spell critic

## 2.1 法术强度和coefficient

**法术伤害总体公式**

> $Amount_{法术}= SpellBase+Coefficient\times SpellPower$

`SpellBase` 指的是技能说明中法术的基础伤害

`Coefficient` 对于不同类型的法术有着不同的计算公式 见下面

---

**计算coefficient的特殊规则**

1. 下面使用的==$T_{PanelCastTime}$==指的是技能面板中初始状态显示的施法时间(==受天赋和装备急速影响之前的施法时间==)
2. 直接(不包括引导型)法术施法时间==$T_{PanelCastTime}$大于7秒的按7秒计算==；==小于1.5秒的按1.5秒计算包括瞬发==；

### 直接伤害/治疗 (direct)

**直接法术伤害公式：**

> $Coefficient = T_{PanelCast Time}/ 3.5 $

---

**直接法术治疗量公式:**

> $Coefficient = (T_{PanelCastTime}/ 3.5) \times 1.88$

---

上面这两个公式的意思是对于技能面板上不同的技能来说法术强度使其拥有的收益是不同的，施法时间越长的法术对法术强度的收益越大，大于7秒和小于1.5秒按照`规则1`来计算收益。

举例来说法师的`火焰冲击`

$T_{火焰冲击} = 0$ (瞬发按照1.5计算)

$Coefficient = 1.5 / 3.5 = 42.86\%$

那么火焰冲击（不算任何天赋加成）的伤害就是 

$Amount_{火焰冲击}= (925 – 1095) + SpellPower \times 42.86\%$

*其中"925-1095"是火焰冲击的SpellBase*

### 非直接类伤害/治疗 (dot/hot)

**dot伤害量计算公式:**

> $$Coefficient = T_{DotDuration} \quad / \quad 15$$

---

**hot治疗量计算公式:**

> $$Coefficient = (T_{HotDuration} \quad / \quad 15) \times 1.88$$

---

举例来说牧师的`暗言术:痛`持续时间18s，一共跳6次，那么计算过程如下

$Coefficient_{暗言术:痛}=18/15=120\%$

每次跳伤害的加成

$Coefficient_{tick} = 120\%/6=20\%$

那么`暗言术：痛`每次跳的伤害就是

$Amount_{tick}=1380/6 + 20\% \times SpellPowerc$

*其中1380是技能的SpellBase*

### 引导类伤害/治疗 (channel)

计算公式和直接法术伤害相同，如果计算每一次伤害的量就除以次数即可。(==大于7秒的施法时间正常计算，不会强制锁定到7秒==)

举例法师的`奥术飞弹` 施法时间5s，一共跳5次，那么计算过程如下

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

### 群体技能 (aoe)

aoe技能必然是一个直接的(direct)法术，如牧师的`治疗祷言`；或是一个引导的(channel)法术，如法师的`暴风雪`，绝不存在aoe技能是dot或hot。

无论是哪种aoe，都是按照direct的公式计算的前提下再乘以50%，公式如下。

**伤害法术:**

> $Coefficient = T_{PanelCastTime} / 3.5 \times 50\%$

---

**治疗法术:**

> $Coefficient = (T_{PanelCastTime} / 3.5) \times 1.88 \times 50\%$

---

==从2.4版本引入一项修改使得一旦受到aoe伤害的目标大于一定数量就不会让每一个个体都受到公式中的伤害；而是这些个体分担某一个总和的伤害，这个公式wowwiki没有给出。==

### 带有特殊效果的技能 (effect)

比如寒冰箭这类除了伤害还带有其他效果的技能在法术强度的收益上会乘以一个系数作为penalty，这个系数每个服务器实现的都不一样，可能一些私服和官服的系数是不一样的，Wowwiki给出的系数是95%。

这些特殊效果的技能可能是直接型的也可能是dot型的，总之都是在原有公式计算的基础上再乘以一个系数。

==1. 计算effect必然是前面包括direct dot/hot channel已经计算完之后再乘这个系数==

==2. 目前的技能并不存在hybrid且带有effect的情况，direct带有effect如法师的`寒冰箭`；dot带有effect如德鲁伊的`虫群`。==

### 兼具伤害和治疗的技能 

有一些技能的描述同时带有伤害和治疗的效果，这种技能典型的如
牧师的 `吞噬瘟疫` `神圣新星`
术士的 `吸取生命`
如`吸血鬼拥抱`这类buff造成的治疗不算这类技能

这类技能wiki没有给出绝对的公式，但是这类技能和hybrid技能一样，符合`守恒定律`，所以可以得出下面的公式

> $Coefficient_{Damage} = Coefficient_{Total} \times \frac{伤害量} {伤害量+治疗量}$
> $Coefficient_{Healing} = Coefficient_{Total} \times \frac{治疗量} {伤害量+治疗量}$

---

这类技能没法通过公式计算，但是可以用这个公式来验证测试出的结果。

下面列出wowwiki给出的分配比例，**用计算出的coefficient乘以这个比例就是真正的coefficient**。

| 技能                               | 分配比例     |
| ---------------------------------- | ------------ |
| 吞噬瘟疫(伤害)<br />吞噬瘟疫(治疗) | 75%<br />25% |
| 吸取生命(伤害)<br />吸取生命(治疗) | 50%<br />50% |
| 神圣新星(伤害)<br />神圣新星(治疗) | 50%<br />50% |

==所以这类技能一定是带有fixed标签，并且我在模拟器中的做法是按照伤害和治疗拆分成不同的技能。==

### 一些例外 (fixed)

说明这类技能的实际coefficient不是公式计算得来的，而是固定的猜测可能是固定设计或是被削弱过。

## 2.2 天赋的影响

**对于法术整体伤害/治疗** (以百分比的形式做乘法)

1. 增加**所有**法术伤害/治疗 (隐藏的，玩家无法直观看到数值只能感受到效果)
2. 增加某一**系**法术伤害/治疗 (隐藏的，玩家无法直观看到数值只能感受到效果)
3. 增加某一**个**法术伤害/治疗 (隐藏的，玩家无法直观看到数值只能感受到效果)
4. 增加某一**个**法术的coefficient (隐藏的，玩家无法直观看到数值只能感受到效果)

**对于法术暴击率** (以百分比的形式做加法)

1. 增加**所有**法术的暴击 (面板上能看到增加)
2. 增加某一**系**法术的暴击 (==据说面板也能看到，需要确认==)
3. 增加某一**个**法术的暴击 (隐藏的，玩家无法直观看到数值只能感受到效果)

**对法术暴击红利** (以百分比的形式做乘法)

1. 增加**所有**法术的暴击红利
2. 增加**某一系**法术的暴击红利

**对于法术急速**

1. 增加**所有**法术的急速百分比 (面板上能看到增加)
2. 减少某一**个**法术的**面板施法时间** (==技能说明上能看到施法时间变化==)

## 2.3 技能属性计算顺序

所有**天赋**和**基础属性**最终都反应在一个技能的**内部属性**上，而这些**内部属性**最终决定了这个技能的所造成的效果的数值。这些属性按照顺序来计算，共分4个阶段如下。

1. 技能的静态数据 
   这部分信息来自没有天赋和属性作用效果时候的技能说明，初始的这部分数据完全是来自游戏的设定信息，所以是完全静态的。
2. 属性
   因为这些值会被天赋使用到，包括`智力`、`精神`、`法术强度` 等。
3. 天赋对技能的影响 
   比如减少技能的施法时间，这个操作一定要在最终在法术急速的作用下计算实际施法时间==之前==就结算，否则就错了。
4. 计算阶段
   在上面的数据确定了之后就可以确定技能的属性了，包括这些属性包括`暴击率`、`实际施法时间`等。

---

**一个技能在不同的阶段确定的属性**

| 阶段         | 技能属性                                                     |
| ------------ | ------------------------------------------------------------ |
| 技能静态数据 | 1. 面板施法时间 (第一次计算)<br />2. coefficient (第一次计算) |
| 属性         | 1. 法术强度 (最终结果)<br />2. 法术暴击 (最终结果)<br />3. 法术急速 (最终结果) |
| 天赋         | 3. 实际面板施法时间(第二次计算，最终结果)<br />5. coefficient (第二次计算，最终结果)<br />6. (所有系/某一系/某一个) **技能数值**加成 (最终结果)<br />7. (某一系/某一个) **法术暴击率**增加 (最终结果)<br />8. (所有系/某一系/某一个) **暴击红利**加成 (最终结果) |
| 计算阶段     | 1. 这个法术的伤害加成<br />2. 这个法术的暴击率<br />3. 这个法术的暴击红利<br />4. 这个法术的实际施法时间<br />5. GCD |

---

**法术最终数值加成**

> $Addition_{法术(最终)} = Addition_{所有法术} + Addition_{所在系} + Addition_{这个法术}$

---

**法术最终暴击率**

> $Critical_{法术(最终)} = Class Constant + (Intellect / 166.6667) +  (Crit Rating / 45.91) + Critical_{所有法术增加} + Critical_{法术所属系增加} + Critical_{这个法术增加} $

---

**法术最终暴击红利**

> $CriticalBonus_{法术(最终)}=CriticalBonus_{法术所属系}+CriticalBonus_{这个法术}$

==$CriticalBonus_{所有系}$的初始值是0.5==

---

**法术实际施法时间**

> $T_{ActualCastTime} = T_{ModifiedPanelCastTime} / (1 + SpellHaste)$

---

**GCD**

> $GCD = 1.5 / (1 + SpellHaste)$

---

==模拟器中没有单独记录"所有法术 提高xx"的记录，而是直接加在了所有系上面，这样更方便维护，详见模拟器代码。==

## 2.4 技能数值最终计算

### 直接法术(读条)

**法术非暴击数值计算**

> $Amount_{法术数值(非暴击)min} = (SpellBase_{min} + SpellPower \times Coefficient)\times Addition_{法术(最终)}$
>
> $Amount_{法术数值(非暴击)max} = (SpellBase_{max} + SpellPower \times Coefficient)\times Addition_{法术(最终)}$

---

**法术暴击数值计算**

> $Amount_{法术数值(暴击)min} = Amount_{法术数值(非暴击)min} \times CriticalBonus_{法术(最终)}$
>
> $Amount_{法术数值(暴击)max} = Amount_{法术数值(非暴击)max} \times CriticalBonus_{法术(最终)}$

---

**法术平均数值计算**

> $Average_{min} = Amount_{法术数值(非暴击)min} \times (1 - Critical_{法术(最终)}) + Amount_{法术数值(暴击)min} \times Critical_{法术(最终)}$
>
> $Average_{max} = Amount_{法术数值(非暴击)max} \times (1-Critical_{法术(最终)}) + Amount_{法术数值(暴击)max} \times Critical_{法术(最终)}$

---

**法术单位时间数值计算**

> $DPS_{法术(非暴击)min} = Amount_{法术数值(非暴击)}/T_{ActualCastTime}$
>
> $DPS_{法术(非暴击)max} = Amount_{法术数值(非暴击)}/T_{ActualCastTime}$

---

### 直接法术(引导)

总体和上面相同，区别在于没有min和max，同时引入了tick的概念。

### 时间性法术

> $Amount_{法术数值(总体)} = (SpellBase + SpellPower \times Coefficient)\times Addition_{法术(最终)}$
>
> $Amount_{法术数值(tick)} = Amount_{法术数值(总体)}/N_{tick}$

---

==WOW的设定dot是不能暴击的，但是3.3.5引入了一些天赋使得dot也可以暴击，如果点了这些天赋就可以把暴击应用到dot的计算上。==

> $Amount_{法术数值(总体暴击)} = Amount_{法术数值(总体)} \times CriticalBonus_{法术(最终)}$
>
> $Amount_{法术数值(tick暴击)} = Amount_{法术数值(总体暴击)}/N_{tick}$

---

### 混合型法术

上述两部分都分析

# 3. 物理技能计算公式

武器技能的critical bonus默认是100%，也就是说默认武器技能暴击得到2倍的伤害，这个数值会被天赋修改。

## 3.1 带有武器伤害的技能

物理技能有不同的计算模型，我把不同的计算模型分为2种，一种是带有`武器伤害`的计算模型，一种不带，先说带`武器伤害`的模型，`武器伤害`分为3种，如下。

- 武器伤害
  - 基础武器伤害 base weapon damage
  - 被AP修改过的武器伤害
    - 非标准化的武器伤害 non-normalized attack-power-modified weapon damage
    - 标准化的武器伤害 normalized attack-power-modified weapon damage

---

`基础武器伤害` 指的是武器的tooltips中展示的伤害范围，*比如`稳固射击`的说明中就提到的“未被修改的武器伤害”指的就是这个*



`非标准化的武器伤害` 指的是人物面板中物理页面中的“近战伤害”(==这里注意一下，要把弹药移除再看面板上的数值==)，这个值用作`自动射击`、`自动攻击`等，也叫`白字伤害`，因为自动攻击在屏幕上的数字是白色的。公式如下 

> $weapon\_dmg_{non-norm} = base\_weapon\_dmg + (T * AP / 14)$

*T是武器的tooltip中的攻速*
*base_weapon_dmg是武器tooltip中的伤害范围*

一些技能使用非标准化的武器伤害，如`奇美拉射击`、`沉默射击`，这类技能的tooltip都标注"百分之xx的武器伤害..."



`标准化的武器伤害` 其实和上面用的公式是相同的，区别是T不来自武器的tooltip，而是固定的，所以叫标准化，固定的数值根据不同的武器类型来决定，如下表

| 武器类型           | T    |
| ------------------ | ---- |
| 匕首               | 1.7  |
| 除匕首外的单手武器 | 2.4  |
| 双手武器           | 3.3  |
| 远程武器           | 2.8  |

==todo wowwiki中说"几乎所有武器伤害技能都受到标准化的影响"，但我实际测试发现不是这样，这个需要确认一下==

我测试的结果

驱散射击这种 “百分之xxx 武器伤害” 都是 非标的 用的是武器实际速度作为系数

瞄准射击 这种 “一次射击” / 致死打死 "一次武器伤害" 都是 标的 用的是 标准化的速度作为系数

## 3.2 不带有武器伤害的技能

除了上面的带有"武器伤害"的计算公式之外，还有不受武器伤害影响的技能，这种技能最终的伤害只受到AP的影响，计算公式如下

> $ability\_dmg = base\_dmg + AP\times coefficient$

其中coefficient就是根据不同的技能有不同的系数了，通过查表即可得到。

举例比如猎人的`毒蛇钉刺`，鼠标放在技能上显示"xx秒造成xxx伤害"，最后的xxx伤害实际上就是已经受到了AP x cofficient之后加成的影响，所以当触发增加AP的饰品buff的时候再把鼠标放在技能上发现这个数值改变了。

## 3.3 弹药对远程武器的伤害加成

远程武器的`武器伤害`除了上面的部分外还有弹药的影响，也就是说，==弹药对远程武器伤害的影响在计算武器伤害的阶段就会计算==。

把鼠标停留在弹药上会显示"增加xxx伤害每秒"，所以根据不同的武器的攻击速度，最终弹药影响`武器伤害`的值是不同的，根据normalize和non-normalize的情况分为下面两种。

---

**non-normalized 远程武器伤害** 

易见到的就是`白字伤害`，实测我使用低级的箭[sharp arrow]-"add 3.5 DPS"，我使用弓[Fine Shortbow]-"10-20 speed 1.7"，实测面板数值提升白字伤害6点，计算如下

> dmg = 3.5 * 1.7 = 5.95

而当我使用284的弓，速度为3.0，实测面板数值提升了11点白字伤害，计算如下

> dmg = 3.5 * 3 = 10.5

---

**normalized 远程武器伤害**

需要乘以的时间参数并不是武器的真实攻速，而是被normalize的时间，根据上面的公式可知，远程武器normalize的时间是2.8，所以这个时间参数就是2.8.

> $dmg_{弹药} = DPS_{弹药} \times 2.8$

由于normalize计算武器伤害也是乘以2.8 所以相当于把tooltip中的"增加dps xxx点"中的xxx直接加上即可。

## 3.4 护甲穿透(ArP)

最开始我理解的护甲穿透就是按照面板上的tootip中的减少护甲的比例乘以目标的护甲，直到我使用了满破的猎人测试发现不是这个情况，我才找到了护甲穿透真实的工作方法。

首先在80级版本，护甲穿透等级(Armor penetration rating)和tooltip中的比例换算的公式是

> $ ArP_{ratio} = ArP_{rating}/14$
>
> 每14点护甲穿透等级 = 1%的护甲减少

我找到的英文的资料如下

> Quote from: Ghostcrawler
>
> *Okay, here is a fairly technical explanation we put together for how armor pen works.*
>
> *We didn’t want Armor Penetration Rating to be too powerful against low armor targets, like it had been in BC. We also didn’t want Armor Penetration Rating to be too powerful against high armor targets.*

我猜测上面的信息是来自暴雪的设计人员的解释，就是说在wlk中，他们设计的ArP希望运行的机制并不是对所有的人物都一样，在TBC中ArP对于布甲表现的太过强势；而同样的也不想对护甲很高的角色杀伤力太高。

> *So, we decided on a system where there is a cap on how much armor the Armor Penetration Rating can be applied to. So, the first X armor on the target is reduced by the percentage listed in the Armor Penetration Rating tooltip, and all armor past that X is unaffected. Another way of understanding that is we multiply the percentage in the tooltip times the minimum of the two values: the cap, and the amount of armor on the target after all other modifiers.*

显然这样就需要设计一个数学公式来限制这个效果，在这个数学公式中，能计算出ArP减少护甲的比例能==作用到的==最多的护甲值，这个值称之为cap，这个cap的存在能达到上面设计的思路和效果，这个公式如下

> cap = "(armor + C) / 3" 和 armor 两者比较的最小的值
>
> armor是当前角色的护甲值，C是一个常数，根据目标等级计算得出，C的计算公式如下
>
> ```
> If (targetlevel < 60)
>    C = 400 + 85 * targetlevel
> Else
>    C = 400 + 85 * targetlevel + 4.5 * 85 * (targetlevel - 59);
> ```

在PVP中，玩家等级都是80，根据上面的公式，计算得出 C=15232.5，==这个值用在护甲减少物理伤害公式中==。

那么举个例子，一个牧师8000护甲，对于这个牧师来说

> armor = 8000
>
> (armor + C) / 3 = 7744
>
> cap是上面两者中的较小的值 所以取7744

这个时候比如我的猎人满破的能忽略100%护甲，这个"忽略100%护甲"的效果只能作用在这个牧师的7744的护甲上，所以忽略了7744 * 100% = 7744护甲，所以在这个猎人造成的物理伤害的过程中，这个牧师的护甲相当于是8000 - 7744 = 256.

从公式其实可以了解到，要想armor > (armor + C) / 3那么护甲就要高于7616.5，==也就是说，在护甲值低于7616.5的情况下，ArP可以完全做用于护甲，一旦目标的护甲值高于7616.5就不可能完全忽略目标的护甲值==

# 4. 补充信息

## 4.1 护甲减少物理伤害

护甲分为几个部分，`基础护甲`(根据属性自带)、`装备护甲`(装备提供)、`魔法护甲`(法术提供 如法师[冰甲术])，所以总和如下公式

>  $armor_{all} = 2 \times Agility+ armor_{grear} + armor_{magic}$

护甲值提供对物理伤害的减伤效果，公式如下(仅提供80级pvp相关)

>  $Reduction = Armor / (Armor + 15232.5)$

15232.5这个数是怎么来的 详见 *护甲穿透(ArP)*

---

实测80级假人的物理减伤是百分之40，因为假人的减伤完全来自护甲，根据上面的公式可以带入计算出，假人的

> 0.4 = X / X + 15232.5
>
> 2X + 15232.5 * 2 = 5X
>
> 所以 X = 10155

最后计算出结果，80级假人的护甲是10155，减伤效果是40%。

## 4.2 pvp韧性减伤

用我的术士打我的法师1372韧性(所有伤害降低29.11% 被暴击率降低14.55% 暴击伤害32.02%)

实测献祭 直接部分 非暴击1101 / 献祭正常非暴击1553 = 70.895% 符合上面降低所有伤害的结果

实测献祭 直接部分 暴击1496 / 献祭正常暴击1552 * 2 = 3104 = 48.195% 这个也符合上面的 如下

> (1-0.2911) * (1 - 0.3202) = 0.481484

1564

## 4.3 技能减伤



## 4.4 增加暴击伤害宝石效果



# 5. 代码实现

代码结构如下

- attribute.py 实现了对技能有影响的属性数据
  - class Attribute 属性
- ability.py 实现了技能相关代码 包括技能静态和计算公式
  - class Spell_ability 魔法技能
  - class Physic_ability 物理技能 其中包含近战和远程物理技能
- mage.py/warlock.py/priest.py.... 实现各个职业天赋对技能的影响
- sim.py 实现模拟器的运行 运行 python3 sim.py --help 可查看帮助

## 5.1 人物属性

人物属性的角度，法系技能伤害和`spell power` `haste` `critical`这几点相关；除此之外还和技能本身的tooltip中提供的伤害相关，两者是叠加关系，所以计算法系伤害之前需要读取==人物面板的属性==。

但是问题来了，人物面板的属性有可能受到天赋的影响，由上文可知有一些天赋影响面板的数值；有一些影响看不到数值只能感受到效果，所以我写模拟器的时候就需要做出选择，"到底是尽量依赖游戏的算法还是尽量自己来通过raw data来计算出这些属性?"，最后我决定还是==尽量依赖游戏的算法==，这样做的好处是减少我自己算错的风险。

模拟器需要模拟天赋对技能的影响，所以我的做法就是

1. 实现天赋的模拟的时候==影响面板数值的天赋都忽略==
2. 直接去拿一个角色==穿好装备且点好天赋==的面板数据

## 5.2 技能分类

另一方面就是技能的分类，上文已经说明了技能的分类，我把这些分类做成了tag，因为这些分类会进行排列组合。在一个csv文件中记录着每个职业法系技能的tag和伤害、基础施法时间等信息，这些信息如下。

- `ability_name` 技能名称
- `ability_type` 技能类型 magic/physical
- `ability_attribute_tags` 技能具备的性质的tag 下文具体说tag的信息
- `panel_cast_time` 未被天赋和急速修改过的施法时间
- `direct_property` 直接的伤害/治疗 数值
  - 直接法术 x-y 其中x是伤害的最小值 y是伤害的最大值 表示一个范围
  - 引导法术 x-y 其中x是伤害总和 y是tick数
- `periodic_property` 周期性的伤害/治疗 数值
  - x-y-z 其中x是伤害总和 y是持续时间 z是tick数
- `school` 技能伤害所属系(仅对魔法技能有用 6个系 冰霜、火焰、奥术、神圣、暗影、自然)
- `database_coefficient` 网站wow-wiki给出的测试出的系数
- `label` 这些法术在指定哪些label的情况下需要测试 (比如冰法就不需要测试 [龙吸术]了) 

在这些中，`spell_attribute_tags`还需要再具体分类，法系技能的tag如下表。

| tag name | explanation                         |
| -------- | ----------------------------------- |
| dmg      | 伤害性法术                          |
| heal     | 治疗法术                            |
| absorb   | 吸收伤害法术                        |
| direct   | 直接性法术                          |
| channel  | 引导型法术                          |
| dot/hot  | 周期性法术                          |
| hybrid   | 具有"直接"和"周期性"的效果          |
| aoe      | aoe型法术                           |
| fixed    | 系数不能使用公式计算 而是一个固定值 |
| effect   | 带有特殊效果 比如 减速 等           |

这些标签对计算公式的影响见上文和代码

物理技能的tag如下表 todo



## 5.3 class Attribute

这个类除了需要的面板属性之外还记录"全局的技能变化"，也就是对某个系或整体所有法术的属性的变化

---

`spell_basic_attr` 字典，包含上文提到的基本数据，包含`spell power` `haste` `critical`这几个数据

---

`spell_critical_increase` 字典，包含不同系法术的法术增加的暴击值，如法师[深冬之寒]增加冰系法术的暴击率

(只有天赋会改变这个变量，且不会显示在面板上)

---

`spell_amount_increase` 字典，包含不同系法术的伤害增加值，如法师[刺骨寒冰]

这个会影响技能的tooltip，所以模拟器读取的静态技能数据都是点天赋之前的tooltip。



## 5.4 class Ability

## 5.5 模拟天赋对技能的修改

**全局**：

1. 增加所有伤害
   		遍历所有.nature是'dmg'的技能 然后增加.specific_amount_increase
2. 增加所有治疗
   		遍历所有.nature是'heal'的技能 然后增加.specific_amount_increase

**法系伤害**：

1. 增加某一个技能伤害
   		增加这个技能的.specific_amount_increase
2. 增加某一个系技能伤害
   		增加self.spell_amount_increase['所属school']
3. 增加所有法术伤害
   		遍历法术技能 增加.specific_amount_increase

**法系治疗**：

1. 增加某一个技能治疗
   		增加这个技能的.specific_amount_increase

**物理**：

	1. 增加某一个技能伤害
		增加这个技能的.specific_amount_increase
	1. 增加近战伤害
	遍历找到所有.ability_type == 'melee'的技能 增加.specific_amount_increase
	1. 增加远程伤害
	遍历找到所有.ability_type == 'ranged'的技能 增加.specific_amount_increase
	1. 增加某一种伤害
	遍历找到所有.school == 某一种类型的技能 增加.specific_amount_increase

# 6. 代码命令及附带工具

## 测试各职业的命令

**法师**

冰法pvp

> python3 sim.py --class=mage --talent=talent_data/mage_frost_pvp.json --attribute=attribute_data/mage_s8_frost.csv

火法pvp

> python3 sim.py --class=mage --talent=talent_data/mage_fire_pvp.json --attribute=attribute_data/mage_s8_fire.csv

---

**牧师**

暗牧pvp

> python3 sim.py --class=priest --talent=talent_data/priest_shadow_2v2.json --attribute=attribute_data/priest_s8_shadow.csv

戒律pvp (急速)

> python3 sim.py --class=priest --talent=talent_data/priest_disc_solo.json --attribute=attribute_data/priest_s8_disc_haste.csv

---

**术士**

毁灭术pvp

> python3 sim.py --class=warlock --talent=talent_data/warlock_destruction_pvp.json --attribute=attribute_data/warlock_s8.csv

痛苦术pvp

> python3 sim.py --class=warlock --talent=talent_data/warlock_affliction_pvp.json --attribute=attribute_data/warlock_s8.csv

---

**猎人**

射击猎人(100%破甲的T10.75)

> python3 sim.py --class=hunter --talent=talent_data/hunter_mm_pvp.json --attribute=attribute_data/hunter_T10_mm.csv

射击猎人(s8)

> python3 sim.py --class=hunter --talent=talent_data/hunter_mm_pvp.json  --attribute=attribute_data/hunter_s8.csv

---

**DK**

> python3 sim.py --class=DK --talent=talent_data/DK_unholy_pvp.json --attribute=attribute_data/DK_s8.csv

## excel天赋dump成json的命令

> ./dump_from_excel.py --input=WOW-talents.xlsx --page=no-talent --start=a2 --end=l12 --type=list > no_talent.json

