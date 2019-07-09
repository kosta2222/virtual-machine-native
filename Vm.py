import sys

class TextWordVm:
  def initBaseTypes(self)->None:
     pass
 
  def initTextWordVector(self,_tVector:list)->None:
    self.tVector=_tVector

  def execute(self)->None:
    
    self.position=0
    isVmWorks=True
    while(isVmWorks):

        tWord=self.tVector[self.position]
        if tWord=='_loads':pass
        elif tWord=='stack':pass
        elif tWord=='end':return
        elif tWord=='}':
          self.position+=1
        else:
           raise Exception('Unknown keyword '+tWord+' at position:'+str(self.position))
           
        self.position+=1               
#===========================
if __name__=='__main__':

  if len(sys.argv)==1:
   print("World of Legends Virtual Machine version 0.1.0 author Arkadiy Vitalyev.")
   exit(1)

  programFileName=sys.argv[1]

  vm=TextWordVm()
  vm.initBaseTypes()
 
  tVector:list=['stack','{','}','end']# отпарсим из файла
  vm.initTextWordVector(tVector)

  vm.execute()
#================================= 

  
