class shapes():
        def _init_(self):
                pass
class Ellipse(shapes):
        def _init_(self,major_axis,minor_axis):
                'major_axis is a,minor_axis is b'
                super(Ellipse,self)._init_()
                self.a=major_axis
                self.b=minor_axis
                
        def compute_circumference(self):
        q=self.a+self.b
        h=(abs((self.a-self.b)/(self.a-self.b)))**2
        m=22/(7*pi)-1
        n=(abs((self.a-self.b)/self.a))**(33.397)
        return pi*q*(1+3*h/(10+(4-3*h)**(0.5)))*(1+m*n)

        def compute_area(self):
        return self.a*self.b*pi
