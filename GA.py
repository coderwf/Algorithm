
# -*- coding:utf-8 -*-
#利用遗传算法求解值

## X + 10 * sin(5*x) + 7 * cos(4*x)
# [0 - 9] 区间最大值
#加入保留五位小数 1.38288 最大位9.00000 = 800000 需要一个
#最大为 900000的二进制数 将其除以10000就得到真实值
# 2^19 - 1 = 524287
# 2^20 - 1 = 1048575 则最少需要20bit
#解设置为
import random
import math
class Ga(object):
    '''
           population_size    = 200      #种群大小
           retention_rate     = 0.2      #存活率
           mutation_rate      = 0.001    #基因突变概率
           select_rate        = 0.6      #自然选择率
           gen_length         = 20       #基因的bit长度
           itms               = 100      #进化代数
           populations        =          #初始化种群
    '''
    def __init__(self,gen_length=20,itms = 0,population_size = 200,retention_rate = 0.2,mutation_rate = 0.01,select_rate = 0.4):
        self.gen_length       = gen_length
        self.itms             = itms
        self.population_size  = population_size
        self.retention_rate   = retention_rate
        self.mutation_rate    = mutation_rate
        self.select_rate      = select_rate
        self.populations      = self.__gen_populations__(population_size,gen_length)
        self.result           = self.populations[0]
    #随机生成一条基因
    def __gen_gene__(self,gen_length):
        origin = 0
        for i in range(0,gen_length):
            if random.randint(0,1) == 0:
                origin = ( origin << 1 ) + 1  #random
            else:
                origin = ( origin << 1 )
        return origin

    #生成population_size条gen_length位的基因,形成一个种群
    def __gen_populations__(self,population_size,gen_length):
        population = []
        for i in range(0,population_size):
            population.append(self.__gen_gene__(gen_length))
        return population

    #将二进制基因解析成为要求的十进制数字,可被子类覆盖
    def decode_to_decimal(self,gene,gen_length):
        return (gene * 9) / float(2 ** gen_length -1)

    #评估函数,评估这条基因对应的适应性数值,可被子类覆盖
    def eval_fun(self,gene):
        decimal_num = self.decode_to_decimal(gene,self.gen_length)
        return decimal_num + 10.0 * math.sin(5 * decimal_num) + 7.0 * math.cos(4 * decimal_num)

    #计算基因的适应度并按照适应度排序返回
    def decode_and_sort(self,population):
        return sorted(population,key = self.eval_fun,reverse=True)

    #mutation 随机变异,某一位刚好变得相反
    def mutation(self,gene,gen_length):
        pos = random.randint(0,gen_length-1)
        mask = 1
        return gene ^ (mask << pos)

    #交叉繁衍产生新的基因
    def cross_propagate(self,male_gene,female_gene,gene_length):
        pos = int(gene_length / 2 )
        mask = 1
        for i in range(0,pos+1):
            mask = (mask << 1) + 1
        femal_c = female_gene & mask
        mask    = 1
        for i in range(0,gene_length - pos -1):
            mask = (mask << 1) + 1
        mask     = mask << (pos + 1)
        male_c   = male_gene & mask
        return femal_c | male_c

    #该种群类进化一次
    def evolve_one_ge(self):
        #优胜劣汰选择,根据淘汰率选择前面的几个
        sort_p = self.decode_and_sort(self.populations)
        pos    = int(self.retention_rate * self.population_size)
        alive , for_sel = sort_p[:pos+1],sort_p[pos+1:]
        #对于剩下的还是有一定概率留下来
        for sel in for_sel:
            if random.random() < self.select_rate:
                alive.append(sel)
        #这时种群数量不足,交叉繁衍产生新的后代
        while len(alive) < self.population_size:
            male   = alive[random.randint(0,len(alive)-1)]
            female = alive[random.randint(0, len(alive) - 1)]
            if male == female:
                continue
            child = self.cross_propagate(male,female,self.gen_length)
            #有一定的几率变异
            if random.random() < self.mutation_rate:
                child = self.mutation(child,self.gen_length)
            alive.append(child)
        self.populations = alive
        #print self.populations

    #itms为进化的代数
    def start_evolve(self,itms):
        for i in range(0,itms):
            self.itms += 1
            self.evolve_one_ge()
        print "evolve ok ..."
        self.result = self.populations[0]
        #print self.decode_to_decimal(self.populations[0],self.gen_length)

    def __str__(self):
        text = {}
        text["population_size"]  = self.population_size
        text["retention_rate"]   = self.retention_rate
        text["mutation_rate"]    = self.mutation_rate
        text["select_rate"]      = self.select_rate
        text["gen_length"]       = self.gen_length
        text["generations"]      = self.itms
        text["excellent"]        = self.decode_to_decimal(self.result,self.gen_length)
        return str(text)

if __name__ == "__main__":
    ga = Ga(population_size=500)
    print ga
    for i in range(0,20):
        ga.start_evolve(10)
        print ga




