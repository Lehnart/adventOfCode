import itertools 

class Computer:

    def __init__(self, A, B, C, program):
        self.A = A
        self.B = B
        self.C = C
        self.program = program 
        self.halt = False 
        self.output = []
        self.instruction_counter = 0
        self.command_by_opcode = { 0:self.adv, 1:self.bxl, 2:self.bst, 3:self.jnz, 4:self.bxc, 5:self.out, 6:self.bdv, 7:self.cdv}
 
    def run(self):
        while 0 <= self.instruction_counter < len(self.program) - 1 and not self.halt:
            command = self.program[self.instruction_counter]
            operand = self.program[self.instruction_counter+1]
            self.command_by_opcode[command](operand)
        return self.output

    def combo_operand(self, value):
        if 0 <= value <= 3 :
            return value 
        if value == 4 :
            return self.A 
        if value == 5 :
            return self.B 
        if value == 6 :
            return self.C 
        
        raise Exception("wrong operand") 
        
    def adv(self, operand):
        num = self.A 
        den = 2**self.combo_operand(operand) 
        self.A = num // den 
        self.instruction_counter += 2 

    def bxl(self, operand):
        self.B = self.B ^ operand 
        self.instruction_counter += 2 
        
    def bst(self,operand):
        self.B = self.combo_operand(operand) % 8 
        self.instruction_counter += 2 
        
    def jnz(self, operand):
        if self.A == 0 :
            self.instruction_counter += 2 
            return
        self.instruction_counter = operand 

    def bxc(self, operand):
        self.B = self.B ^ self.C
        self.instruction_counter += 2 
        
    def out(self, operand):
        self.output.append( self.combo_operand(operand) % 8 ) 
        if self.output != self.program[:len(self.output)]:
            self.halt = True  
            return 
        if self.output == self.program :
            self.halt = True
        self.instruction_counter += 2 
    
    def bdv(self, operand):
        num = self.A 
        den = 2**self.combo_operand(operand) 
        self.B = num // den 
        self.instruction_counter += 2 

    def cdv(self, operand):
        num = self.A 
        den = 2**self.combo_operand(operand) 
        self.C = num // den 
        self.instruction_counter += 2 

    def __str__(self):
        return f"A: {self.A}, B: {self.B}, C: {self.C}"

max_len = 0 
a = -1
program = [2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0]
d = {}
min_len = 12
bins = 18
ok = ['010101111010111111', '010101111001101101'] 

for p in itertools.product("01", repeat = 30):
    b = "0b"+"".join(p)
    for o in ok : 
        a = int(b+o, 2)
        comp = Computer(a,0,0,program)
        output = comp.run()
        if len(output) >= min_len :
            if (bin(a)[-bins:] not in d):
                d[bin(a)[-bins:]] = 0 
            d[bin(a)[-bins:]] += 1

        if len(output) > max_len :
            max_len = len(output)
            print(max_len, a, output, program)
print(d)