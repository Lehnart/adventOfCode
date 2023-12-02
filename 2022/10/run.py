class Cpu:

    def __init__(self):
        self.X = 1
        self.n_cycles = 0
        self.power = 0
        self.save_cycles = [20, 60, 100, 140, 180, 220]
        self.screen = ""

    def process(self, cmd: str):
        previous_cycle = self.n_cycles
        previous_X = self.X

        if "noop" in cmd:
            self.draw()
            self.n_cycles += 1
        if "add" in cmd:
            self.draw()
            self.draw()
            _, n = cmd.strip().split()
            n = int(n)
            self.n_cycles += 2
            self.X += n

        if len(self.save_cycles) > 0 and previous_cycle <= self.save_cycles[0] < self.n_cycles:
            cycle = self.save_cycles.pop(0)
            self.power += previous_X * cycle

    def draw(self):
        if self.X - 1 <= len(self.screen)%40 <= self.X + 1:
            self.screen += "#"
        else:
            self.screen += "."


cpu = Cpu()
with open("input.txt") as file:
    for line in file:
        cpu.process(line)
    print(cpu.power)
    for i in range(len(cpu.screen)//40):
        print(cpu.screen[i*40:(i+1)*40])
