class Solution:
    def studentGrade(self, marks):
        if marks>=90:
            print("Grade A")
        elif marks>=70:
            print("Grade B")
        elif marks>=50:
            print("Grade C")
        elif marks>=35:
            print("Grade D")
        else:
            print("Fail")
            

cls = Solution()
marks =[90, 70, 50, 35, 20, 100, 80, 60, 40, 30]
for i in marks:
    cls.studentGrade(i)
    print("------------")
    