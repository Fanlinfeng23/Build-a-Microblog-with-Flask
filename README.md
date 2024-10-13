# datalab 报告

姓名：范林峰

学号：2023200424

| 总分 |bitXor|logtwo|byteSwap|reverse|logicalShift|leftBitCount｜float_i2f｜floatScale2｜ float64_f2i｜floatPower2｜
| --------- | ------------- | ------------- | ------------- | ----------------- |-----------|--------- |--------- |--------- |--------- |--------- |
|36/36|1/1|2/2|4/4|4/4|3/3|3/3｜4/4｜4/4｜4/4｜3/3｜4/4｜


test 截图：

![image](./imgs/image.png)

<!-- TODO: 用一个通过的截图，本地图片，放到 imgs 文件夹下，不要用这个 github，pandoc 解析可能有问题 -->

## 解题报告

### 亮点



1. reverse
2. float_i2f
3. bitXor
4. byteswap
5. samesign
6. logtwo
7. floatScale2
8. logicalShift
9. floatPower2
10. float64_f2i
11. leftBitCount

### bitXor

```c
int bitXor(int x, int y) {
    return (~(x & y)) & (~((~x) & (~y)));
}
```

题目思路


#### 1. 先分析XOR (异或) 的逻辑：
异或运算符 ^ 的特点是：只有当两个二进制位不同（一个是 0，一个是 1）时结果才为 1。
也就是说：x ^ y = (x 或 y 为 1，但不能同时为 1)。

#### 2. 转化成合法运算符：
根据题目要求，使用 ~（按位取反）和 &（按位与）来模拟 ^。

#### 3. 逻辑表达式拆解：
考虑~(x & y)：当 x 和 y 的位同时为 1 时，取反后变成 0。
相反地，~(~x & ~y)：当 x 和 y 的位同时为 0 时，取反后变成 0。
两者的 & 结果就是 XOR 的结果。

### samesign
```c
int samesign(int x, int y) {
    if ((!((x ^ y) >> 31))  && x && y) return 1;
    if ((!x) && (!y)) return 1;
    else return 0;
    
}
```
解题思路

#### 1. 首先进行符号位的判断：
一个整数的符号位在二进制表示的最高位（第 31 位），0 表示非负数，1 表示负数。

#### 2. x ^ y 的符号异或：
在x ^ y过程中，主要关注符号位：符号不同时，最高位为 1；符号相同时，最高位为 0。

#### 3. (x ^ y) >> 31：移位后，结果为 1（不同符号）或 0（相同符号）。另外，由于0的符号位和正数相同，我们要排除0和正数进行比较的情况，所以在后面加入 &x &y 。如果有一个数为0，则不返回1.

#### 4. 处理 0 的情况：
如果 x 和 y 都是 0，则结果为同号。




### logtwo
```c
int logtwo(int v) {
    int x = ((v >> 16) > 0) << 4;
    v = v >> x;
    
    int shift = ((v >> 8) > 0) << 3;
    v = v >> shift;
    x = x|shift;


    shift = ((v >> 4) > 0) << 2;
    v = v >> shift;
    x = x|shift;
    
    shift = ((v >> 2) > 0) << 1;
    v = v >> shift;
    x = x|shift;
    
    shift = ((v >> 1) > 0) << 0;
    v = v >> shift;
    x = x|shift;
    
    
    return x;
}
```
解题思路

#### 1. 首先，根据题目要求的运算规律，我们求的logtwo即为寻找二进制的最高非零位（不考虑负数）。例如，32 = 2^5，因此其 log2 为 5。

#### 2. 采取逐步移位判断：
由于没有循环，我们采取2的n次幂唯一的方式来寻找准确值。
首先将 v 右移 16 位，检查高 16 位是否有 1，如果有，将 x 加 16。
接下来继续移位（8、4、2、1），逐步找到最高位的准确位置。

#### 3. 对结果取｜或：
由于我们每次得到的shift值都是在只有第n-1位上可能为1，想要把他们相加，只需取或即可。
这种实现方式避免了循环，通过移位高效计算二进制对数。

### byteswap
```c
int byteSwap(int x, int n, int m) {
    n = n << 3;
    m = m << 3;
    int y = ((x >> n ) & 0xFF) << m;
    int z = ((x >> m ) & 0xFF) << n;
    x = x & (~(0xFF << n));
    x = x & (~(0xFF << m));
    return x | y | z;
}
```
解题思路

#### 1. 由于题目要求按字节进行提取，所以我们要先将m，n各自乘以8，得到新的m，n。

#### 2. 提取字节：
使用 (x >> n) & 0xFF 提取第 n 个字节，m同理。即可得到m，n所在的各自八位的字节。

#### 3. 清空原始字节位置：
使用 ~(0xFF << n) 清除第 n 和 m 个字节。使其对应位置置0.

#### 4.合并结果：
将交换后的字节与原始数据合并，对取出的m，n所在字节以及置零后的x取或操作，即可得到最终结果。
### reverse
```c
unsigned reverse(unsigned v) {
    unsigned a = (0xAAAAAAAA & v) >> 1;
    unsigned b = (0x55555555 & v) << 1;
    v = a | b;
    a = (0xCCCCCCCC & v) >> 2;
    b = (0x33333333 & v) << 2;
    v = a | b;
    a = (0xF0F0F0F0 & v) >> 4;
    b = (0x0F0F0F0F & v) << 4;
    v = a | b;
    a = (0xFF00FF00 & v) >> 8; 
    b = (0x00FF00FF & v) << 8;
    v = a | b;
    a = (0xFFFF0000 & v) >> 16;
    b = (0x0000FFFF & v) << 16;
    v = a | b;
    
    return v;
}
```
解题思路

#### 1. 基本思路：逐步交换相邻位：

(1)按位分组处理：这段代码逐步对 32 位整数中的位进行交换，从最低位到最高位，采用“分治法”逐步交换越来越大的位组。这步的主要意图就是先两两对换，再四四对换...保证每次对换后，在小范围内都会实现了反转，最后逐步扩展到32位。

(2)分解掩码逻辑：每次使用特定的掩码与输入进行按位与（&），然后分别左移或右移后通过按位或（|）合并。
0xAAAAAAAA 是一个交替出现 1 和 0 的掩码：101010...
0xCCCCCCCC 是两个相邻 1 后跟两个 0：11001100...
其他掩码以此类推（每次掩码覆盖的位数加倍）。

#### 2. 第一步：交换相邻的位
代码：
```c
v = ((v & 0xAAAAAAAA) >> 1) | ((v & 0x55555555) << 1);
```
目的：将奇数位和偶数位进行交换。
将 0xAAAAAAAA 和 v 进行按位与，提取所有奇数位，然后将它们右移 1 位。
将 0x55555555 和 v 进行按位与，提取所有偶数位，然后将它们左移 1 位。
最后合并两部分，实现奇偶位交换。
#### 3. 第二步：每 2 位一组进行交换
代码：
```c
v = ((v & 0xCCCCCCCC) >> 2) | ((v & 0x33333333) << 2);
```
目的：每两位为一组进行交换。
使用 0xCCCCCCCC 提取高两位，然后右移 2 位。
使用 0x33333333 提取低两位，然后左移 2 位。
合并后完成每 2 位的交换。
#### 4. 第三步：每 4 位一组交换
代码：
```c
v = ((v & 0xF0F0F0F0) >> 4) | ((v & 0x0F0F0F0F) << 4);
```
目的：每 4 位为一组进行交换。
#### 5. 第四步：每 8 位一组交换
代码：
```c
v = ((v & 0xFF00FF00) >> 8) | ((v & 0x00FF00FF) << 8);
```
#### 6. 第五步：交换高 16 位和低 16 位
代码：
```c
return (v >> 16) | (v << 16);
```

### logicalshift
```c
int logicalShift(int x, int n) {
    int mask = ~(((1 << 31) >> n) << 1);  
    return (x >> n) & mask;  
}
```
解题思路

#### 1. 针对该问题，在 C 中，右移操作符 >> 对有符号整数进行算术右移，即用符号位填充高位。如果要实现逻辑右移（用 0 填充高位），需要手动构造掩码来处理。

#### 2. 构造掩码
```c
int mask = ~(((1 << 31) >> n) << 1);
```
1 << 31：将数字 1 左移 31 位，得到最高位为 1，其余位为 0 的二进制数。 
>> n：右移 n 位，产生一个右移后的高位掩码，前n+1位为1，后面全为0。
<< 1：再将掩码左移 1 位，对齐逻辑右移的效果。
这样做而非直接右移n-1位的目的是为了防止n=0时出现错误。
~：按位取反，得到逻辑右移所需的掩码。

#### 3. 应用掩码
右移并与掩码相与：
```c
return (x >> n) & mask;
```
使用算术右移计算出的结果与掩码按位与，确保高位补 0，实现逻辑右移的效果。


### leftBitCount
```c
int leftBitCount(int x) {
    int y = x ^ 0xFFFFFFFF;
    int T = (!y) ;
    int a = (! (! (y >> 16))) << 4;
    y = y >> a;
    
    int b = (! (! (y >> 8))) <<3;
    y = y >> b;

    int c = (! (! (y >> 4))) <<2;
    y = y >> c;

    int d = (! (! (y >> 2))) <<1;
    y = y >> d;

    int e = (! (! (y >> 1))) <<0;
    y = y >> e;

    int bitcount = ((~(a|b|c|d|e)) ^ 32) & 0x0000001F;


    return (T<<5) | ((((!T)<<4)|((!T)<<3)|((!T)<<2)|((!T)<<1)|(!T))&bitcount) ;
}
```
解题思路：

#### 1. 整体思路：
将输入 x 的二进制反转，变成找左侧连续 0的问题（即：将所有 1 翻转为 0，将所有 0 翻转为 1）。
通过逐层检查 16 位、8 位、4 位、2 位和 1 位，缩小范围，直到找到第一个非 0 位的位置。
最后使用位移和掩码计算总的连续 1 数。

#### 2. 详细解题思路：
(1) 步骤 1：翻转所有位
```c
int y = x ^ 0xFFFFFFFF;
```
用 x ^ 0xFFFFFFFF 将 x 的所有位取反。
原问题是统计左侧连续 1 的数量，取反后等价于统计左侧连续 0 的数量。
(2) 步骤 2：检查 y 是否全为 0，排除特殊情况，二分只能查找1-31之间的数，故32时需要单独讨论。
```c
int T = (!y);
```
使用 !y 判断 y 是否为 0：
如果 y 为 0，说明原始的 x 中全是 1（即连续 1 的数量是 32），T = 1。
如果 y 非 0，则 T = 0，需要继续查找连续 1 的数量。

（3）步骤 3：逐步二分查找连续 0 的位置
第一级：检查高 16 位是否有非 0 位
```c
int a = (!(! (y >> 16))) << 4;
y = y >> a;
```
先将 y 右移 16 位，判断最高的 16 位是否全为 0：
如果全为 0，则结果为 0；否则为 1。
使用 (! (! ...)) 结构将结果强制转换为 0 或 1。
如果最高 16 位存在非 0 位，将 a 置为 16（即 1 << 4）。
接着将 y 右移 a 位，缩小搜索范围。

第二级：检查剩下的高 8 位
用类似逻辑检查接下来的 8、4、2、1 位，并根据结果决定是否再右移。

(4) 步骤 4：计算连续 1 的总数

```c
int bitcount = ((~(a | b | c | d | e)) ^ 32) & 0x0000001F;
```
a | b | c | d | e 表示在各级检查中右移的总位数。
~(...) ^ 32 用于计算连续 1 的数量：
由于我们统计的是连续 0 的数量，因此需要用 32 - (总位数) 得到连续 1 的数量。
& 0x0000001F 用于限制结果在 0 到 31 之间。

(5)步骤 5：处理特殊情况（全为 1 的情况）
```c
return (T << 5) | ((((!T) << 4) | ((!T) << 3) | ((!T) << 2) | ((!T) << 1) | (!T)) & bitcount);
```
判断是否全为 1：
如果 T = 1，说明原数 x 全是 1，此时结果直接是 32（T << 5）。
如果 T = 0，则返回计算的 bitcount。

### float_i2f
```c
unsigned float_i2f(int x) {

    if(!x) return 0;
    if(x==0x80000000) return 0xcf000000;

    int sign = x & 0x80000000;
    
    if(sign) x = ~x+1;
    int count = 30;
    while(!(x&(1<<count))) count--;
    if(count <= 23){
        x<<=(23 - count);
    } 
    else{
        x+=(1<<(count - 24));
        int y=x<<(55 - count);
        if(y) ;else x&=(0xffffffff<<(count - 22));
        if(x&(1<<count))  ;else count++;
        x >>= (count-23);
    }

    x = x & 0x007fffff;
    count = (count + 127) << 23;
    return x|count|sign;
}
```
### `float_i2f` 每一步详细解题思路

此函数的任务是将一个 **32 位整数**转换为 **IEEE 754 单精度浮点数**的位级表示。单精度浮点数包含三部分：符号位 (1 bit)、指数位 (8 bits) 和尾数位 (23 bits)。下面是代码每一部分的详细解题思路：



#### 1. **特殊情况处理**
```c
if (!x) return 0;
if (x == 0x80000000) return 0xcf000000;
```
- **`if (!x)`**: 如果输入整数 `x` 是 0，则直接返回浮点表示的 0（即所有位为 0 的 32 位无符号整数）。
- **`if (x == 0x80000000)`**: 检查输入是否为最小负数（`INT_MIN`），即 -2³¹。  
  - **理由**：`INT_MIN` 的浮点表示是一个特殊值，二进制为 `0xcf000000`。


#### 2. **提取符号位**
```c
int sign = x & 0x80000000;
```
- **操作**：提取 `x` 的最高位（符号位），这是浮点数符号部分的内容。  
  - 如果符号位为 1，则代表负数；否则为正数。


#### 3. **将负数取反求补**
```c
if (sign) x = ~x + 1;
```
- 如果 `x` 是负数，则将其转换为相应的正数形式（取反加 1）。


#### 4. **寻找最高位 1 的位置**
```c
int count = 30;
while (!(x & (1 << count))) count--;
```
- **操作**：通过逐位检查找到二进制表示中最高位 1 的位置（从高位向低位查找）。  
  - 例如：对于 `x = 0b100110`，最高位 1 在第 5 位。


#### 5. **对齐到尾数部分（23 位）**
```c
if (count <= 23) {
    x <<= (23 - count);
}
```
- 如果最高位 1 的位置在 **23 位以内**，将其左移，使最高位对齐到 23 位的位置。


#### 6. **四舍五入处理**
```c
else {
    x += (1 << (count - 24));
    int y = x << (55 - count);
    if (y) ; else x &= (0xffffffff << (count - 22));
    if (x & (1 << count)) ; else count++;
    x >>= (count - 23);
}
```
- 如果最高位 1 在 23 位 **之后**，需要进行 **右移**，并执行 **四舍五入**：
  1. `x += (1 << (count - 24))`: 向尾数的第 24 位加 1，实现四舍五入。
  2. `int y = x << (55 - count)`: 检查是否存在舍去部分的非零位。
  3. 如果不存在舍去部分，则将低位清零。
  4. 右移，确保尾数只保留 23 位。


#### 7. **构造浮点数的尾数和指数部分**
```c
x = x & 0x007fffff;
count = (count + 127) << 23;
```
- **尾数部分**：`x & 0x007fffff` 将多余的位清除，只保留 23 位尾数。
- **指数部分**：`count + 127` 将偏置值 127 加到指数上，并将结果左移 23 位，形成浮点数的指数部分。


#### 8. **拼接浮点数表示**
```c
return x | count | sign;
```
- 使用 **按位或运算**将符号位、指数部分和尾数部分拼接起来，形成最终的浮点数表示。



### floatScale2
```c
unsigned floatScale2(unsigned uf) {
    unsigned sign = uf & 0x80000000;
    unsigned exponent = (uf >> 23) & 0xFF;
    unsigned fraction = uf & 0x7FFFFF;

    if (exponent == 0xFF) {
        return uf;
    }
    if (exponent == 0) {
        fraction <<= 1;
    } else {
        exponent++;
    }

    return sign | (exponent << 23) | fraction;
}
```
解题思路

#### 1. **提取符号位、指数部分和尾数部分**
```c
unsigned sign = uf & 0x80000000;
unsigned exponent = (uf >> 23) & 0xFF;
unsigned fraction = uf & 0x7FFFFF;
```
- **符号位**：`uf & 0x80000000` 提取浮点数的最高位（符号位），用于判断正负数。
- **指数部分**：`(uf >> 23) & 0xFF` 提取浮点数的指数部分（8 位）。
  - 指数部分用于控制浮点数的大小，存储的是偏置指数（偏置值为 127）。
- **尾数部分**：`uf & 0x7FFFFF` 提取浮点数的尾数部分（23 位）。



#### 2. **特殊情况：NaN 和无穷大**
```c
if (exponent == 0xFF) {
    return uf;
}
```
- **操作**：检查指数部分是否为 `0xFF`（即 **全 1**）。  
  - 如果是，表示输入浮点数是 **NaN（Not a Number）** 或 **无穷大**，此时直接返回原数 `uf`。
  - **理由**：对 NaN 或无穷大执行任何数学运算，都应该返回原值。



#### 3. **判断是否是非规格化数**
```c
if (exponent == 0) {
    fraction <<= 1;
} else {
    exponent++;
}
```
- **非规格化数**：  
  - 如果指数部分为 0，表示输入为 **非规格化数**（即指数为 0，尾数非 0）。  
  - 对于非规格化数，将尾数左移 1 位，实现数值的 2 倍扩展。

- **规格化数**：  
  - 如果指数不为 0，表示输入是 **规格化数**。  
  - 对规格化数，只需要将指数部分加 1，即数值扩大 2 倍。


#### 4. **拼接符号、指数和尾数**
```c
return sign | (exponent << 23) | fraction;
```
- 使用 **按位或运算** 将符号位、指数部分和尾数部分重新拼接起来，形成新的浮点数的位级表示。



### float64_f2i
```c
int float64_f2i(unsigned uf1, unsigned uf2) {
    int sign=uf2 >> 31;
    
    int e =((uf2 & 0x7FF00000) >> 20) - 1023;
    if(e < 0) return 0;
    if(e > 30) return 0x80000000;

    unsigned us=((uf2 & 0xFFFFF) << 11)|(uf1 >> 21);
    us=(us >>(31 - e))|(1 << e ); 
    if(!sign)
    return us;
    else
    return - us;
}

```
解题思路

将一个 **64 位的 IEEE 754 双精度浮点数**转换为 **32 位的有符号整数**。  
浮点数采用 IEEE 754 标准格式，由符号位、指数位和尾数组成。  
双精度浮点数具体结构：
- **符号位** (1 bit)
- **指数部分** (11 bits，偏置值为 1023)
- **尾数部分** (52 bits)


#### 1. **提取符号位**
```c
int sign = uf2 >> 31;
```
- **操作**：提取浮点数的 **符号位**（第 63 位），用于判断该数是否为负数。
  - `sign = 0`：正数。
  - `sign = 1`：负数。



#### 2. **提取指数部分并计算有效指数**
```c
int e = ((uf2 & 0x7FF00000) >> 20) - 1023;
```
- **操作**：
  1. 从高 32 位 `uf2` 中提取 **指数部分**（第 52-62 位）。
     - `(uf2 & 0x7FF00000)`：将高 32 位中的指数部分提取出来。
     - `>> 20`：右移 20 位得到 11 位的指数值。
  2. 将提取的指数减去 **偏置值 1023**，得到浮点数的有效指数 `e`。
     - 该指数表示浮点数中二进制数值的位置。


#### 3. **处理下溢情况**
```c
if (e < 0) return 0;
```
- **操作**：如果指数 `e < 0`，说明浮点数的值非常接近 0，无法表示为非 0 的整数。
  - **返回值**：直接返回 0。



#### 4. **处理上溢情况**
```c
if (e > 30) return 0x80000000;
```
- **操作**：如果指数 `e > 30`，则浮点数的值超出了 32 位整数的表示范围。
  - **返回值**：返回 `0x80000000` 作为溢出标志。



#### 5. **提取并处理尾数部分**
```c
unsigned us = ((uf2 & 0xFFFFF) << 11) | (uf1 >> 21);
```
- **操作**：
  1. 从 `uf2` 的低 20 位提取尾数部分（即第 0-51 位中的高 20 位）。
     - `(uf2 & 0xFFFFF)`：获取高位部分的尾数。
  2. 将高位尾数左移 11 位，与 `uf1` 中的前 21 位拼接成 **有效尾数**。
     - `uf1 >> 21`：从 `uf1` 中获取低 32 位的高 21 位。
     - 使用按位或 `|` 将两部分拼接。


#### 6. **调整尾数与指数匹配**
```c
us = (us >> (31 - e)) | (1 << e);
```
- **操作**：
  1. 根据有效指数 `e`，将尾数 **右移 `(31 - e)`** 位，使其对齐为整数。
  2. 使用 `| (1 << e)` 表示隐含的最高位 `1`，它是标准浮点数格式的一部分。



#### 7. **处理符号位，返回结果**
```c
if (!sign)
    return us;
else
    return -us;
```
- **操作**：根据符号位决定返回值的正负：
  - 如果 `sign = 0`，返回正数 `us`。
  - 如果 `sign = 1`，返回负数 `-us`。



### floatPower2
```c
unsigned floatPower2(int x) {
    unsigned exp;
    if (x < -126) {
        return 0; 
    } else if (x > 127) {
        return 0x7F800000; 
    } else {
        exp = x + 127; 
        return exp << 23; 
    }
}
```
解题思路

单精度浮点数结构（IEEE 754 标准）：
- **符号位**：1 bit
- **指数部分**：8 bits（带偏置值 127）
- **尾数部分**：23 bits（小数部分，不包括隐含的1）

1. **指数部分的计算**：根据给定的 `x`，计算偏置后的指数值。
2. **特殊情况处理**：
   - 如果 `2.0^x` 太小无法表示为浮点数，返回 0（下溢）。
   - 如果 `2.0^x` 太大超过浮点数的表示范围，返回正无穷大（+∞）。


#### 1. **变量声明**
```c
unsigned exp;
```
- **操作**：声明一个无符号整数 `exp`，用于存储计算得到的 **指数部分**。



#### 2. **下溢情况处理**
```c
if (x < -126) {
    return 0;
}
```
- **操作**：
  - 如果 `x < -126`，表示 \(2.0^x\) 太小，无法表示为最小的 **非规格化浮点数**。
  - **返回值**：直接返回 0，表示浮点数为 0。


#### 3. **上溢情况处理**
```c
else if (x > 127) {
    return 0x7F800000;
}
```
- **操作**：
  - 如果 `x > 127`，表示 \(2.0^x\) 太大，超出浮点数的表示范围。
  - **返回值**：返回 `0x7F800000`，即浮点数的 **+∞** 表示形式。
  - `0x7F800000` 的二进制结构：
    - **符号位**：0（正数）
    - **指数部分**：全为 1，即 `11111111`（表示无穷大）
    - **尾数部分**：全为 0。


#### 4. **正常指数计算**
```c
exp = x + 127;
```
- **操作**：
  - 计算浮点数的 **指数部分**，即将给定的指数 `x` 加上偏置值 `127`。
  - IEEE 754 标准规定，浮点数的指数部分是带 **偏置值 127** 的。
    - 例如：对于 \(2.0^0\)，`x = 0`，指数部分应为 `0 + 127 = 127`。



#### 5. **构造浮点数的二进制表示并返回**
```c
return exp << 23;
```
- **操作**：
  - 将计算得到的 **指数部分** 左移 23 位，将其存入浮点数的 **指数字段**。
    - **符号位**为 0（正数）。
    - **尾数部分**为 0（因为 \(2.0^x\) 的尾数部分为隐含的1，且没有小数部分）。
  - 返回最终构造的浮点数的 **二进制表示**。



## 反馈/收获/感悟/总结

虽然整体的实现花费时间较长，但我觉得确实学到了很多，而且我觉得比较好的一点是不再针对运算符的数量进行无谓的内卷，这样能使作业的压力减轻许多。

首先，我基本掌握了有关灵活处理位运算的基本操作，能够较为熟练地使用各种逻辑和位移运算符。

其次，我通过本次lab更深入地巩固了整数和浮点数的知识。对他们也有了更加深入的理解。

最后，我还学会了本地与云端的代码协作与交互，开始接触使用github 和 git等。



## 参考的重要资料

<!-- 有哪些文章/论文/PPT/课本对你的实现有重要启发或者帮助，或者是你直接引用了某个方法 -->

<!-- 请附上文章标题和可访问的网页路径 -->
