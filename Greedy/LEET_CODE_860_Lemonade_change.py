class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cost_5, cost_10 = 0, 0 # 내가 가진 $5, $10 를 저장하는 변수
        for bill in bills:
            if bill==5: # 고객이 $5를 지불했을 때
                cost_5+=1 
            elif bill==10: # 고객이 $10를 지불했을 때
                if cost_5>0: # 내가 $5를 1개 이상 가지고 있으면
                    cost_10+=1 
                    cost_5-=1 
                else: return False 
            else: # 고객이 $20를 지불했을 때
                if cost_10>0 and cost_5>0: # 내가 $10와 $5를 각 한개 이상씩 가지고 있으면
                    cost_10-=1 
                    cost_5-=1
                elif cost_5>2: # 내가 $5를 3개 이상 가지고 있으면
                    cost_5-=3
                else: return False
        return True
