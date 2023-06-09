import requests
import json
class Produkts:
    def __init__(self, nosaukums, cena, apraksts):
        self.nosaukums = nosaukums
        self.cena = cena
        self.apraksts = apraksts

    def get_nosaukums(self):
        return self.nosaukums
    def set_nosaukums(self, n):
        self.nosaukums = n

    def get_cena(self):
        return self.cena
    def set_cena(self, n):
        self.cena = n


    def get_apraksts(self):
        return self.apraksts
    def set_apraksts(self, n):
        self.apraksts = n


class Elektronika(Produkts):
    def __init__(self, nosaukums, cena, apraksts,jauda):
        super().__init__(nosaukums, cena, apraksts)
        self.jauda = jauda
    def get_jauda(self):
        return self.jauda
    def set_jauda(self, n):
        self.jauda = n


class Apgerbs(Produkts):
    def __init__(self, nosaukums, cena, apraksts,izmers):
        super().__init__(nosaukums, cena, apraksts)
        self.izmers = izmers
    def get_izmers(self):
        return self.izmers
    def set_izmers(self, n):
        self.izmers = n

class Gramata(Produkts):  
    def __init__(self, nosaukums, cena, apraksts,lappuses):
        super().__init__(nosaukums, cena, apraksts)
        self.lappuses = lappuses
    def get_lappuses(self):
        return self.lappuses
    def set_lappuses(self, n):
        self.lappuses = n


class Grozs:
    def __init__(self):
        self.saturs = []

    def pievienot(self,prece,skaits=1):
        ok = True
        for i in range(len(self.saturs)):
            (p,s) = self.saturs[i]
            if p == prece:
                s = s+1
                self.saturs[i] = (p,s)
                ok = False
        if ok:
            self.saturs.append((prece,skaits))

    def dzest(self,prece):
      
        for i in range(len(self.saturs)):
            (p,s) = self.saturs[i]
            
            if p == prece:
                s = s-1
                self.saturs[i] = (p,s)
                
                if s == 0:
                   k = (p,s)
                   self.saturs.remove(k) 
                   break
        


                
            
            

    def kopums(self):
        if self.saturs == []:
            print("Grozs ir tukšs")
        else:
            print("Groza saturs:")
            count =1 
            for i in range(len(self.saturs)):

                if self.saturs[i][1] > 0:
                    
                    print("{}: nosaukums: {} cena: {} apraksts: {}".format(count,self.saturs[i][0].get_nosaukums(), self.saturs[i][0].get_cena(),self.saturs[i][0].get_apraksts()))
                    count = count +  1


    def kopeja_vertiba(self,kurss):
        def vertiba_sum(self):
            total = 0
            for i in range(len(self.saturs)):
                (p,s) = self.saturs[i]
                total += p.get_cena()*s
            return total
        if kurss == 'EUR':
            vertiba = vertiba_sum(self)
            print('Kopējā vērtība: {}'.format(vertiba)+'EUR')
        else:
            api = 'http://open.er-api.com/v6/latest/EUR'
            response = requests.get(api)
            if response.status_code == 200:
                # Request was successful
          
                data = response.text
                data = json.loads(data)
                reiznatajs = data['rates'][kurss]
                vertiba = vertiba_sum(self)
                print('Kopējā vērtība: {}'.format(vertiba*reiznatajs)+ kurss)
            else:
                # Request failed
                print("Neizdevās savienoties ar serveri:", response.status_code)

        
    
def main():
    g = Grozs()
    tehnika = Elektronika('iphone',500,'no Apple',1000)
    kanceleja = Gramata('Sola',5,'no G. Janovska',300)
    virsdrebes = Apgerbs('t-krekls',130,'no Pakistanas','XL')

    print(virsdrebes.get_izmers())
    g.pievienot(tehnika)
    g.pievienot(kanceleja,100)
    g.pievienot(virsdrebes)
    g.kopeja_vertiba('USD')
    g.kopums()
    g.dzest(tehnika)
    g.kopums()
    g.kopeja_vertiba('EUR')

if __name__ =='__main__':
    main()