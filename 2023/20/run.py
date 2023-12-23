import enum
from typing import List

LOW_COUNT, HIGH_COUNT = 0, 0
CYCLE = 0

class SignalType(enum.Enum):
    LOW = 0
    HIGH = 1


class Signal:

    def __init__(self, type: SignalType, dest: str, source: str):
        self.type = type
        self.dest = dest
        self.source = source


class Broadcaster:

    def __init__(self, name: str, destinations: List[str]):
        self.destinations = destinations
        self.name = name

    def process(self, signal: Signal):
        return [Signal(signal.type, d, self.name) for d in self.destinations]


class FlipFlop:

    def __init__(self, name: str, destinations: List[str]):
        self.state = False
        self.name = name
        self.destinations = destinations

    def process(self, signal: Signal):
        if signal.type == SignalType.HIGH:
            return []
        if not self.state:
            self.state = True
            return [Signal(SignalType.HIGH, d, self.name) for d in self.destinations]
        if self.state:
            self.state = False
            return [Signal(SignalType.LOW, d, self.name) for d in self.destinations]


class Conjunction:

    def __init__(self, name: str, destinations: List[str]):
        self.inputs = {}
        self.destinations = destinations
        self.name = name

    def add_input(self, name: str):
        self.inputs[name] = SignalType.LOW

    def process(self, signal: Signal):
        self.inputs[signal.source] = signal.type
        if self.name == "gf":
            #if any(self.inputs[i] == SignalType.HIGH for i in self.inputs):
            if self.inputs["qk"] == SignalType.HIGH :
                print(CYCLE)
                print(self.inputs)

        if all(t == SignalType.HIGH for t in self.inputs.values()):
            return [Signal(SignalType.LOW, d, self.name) for d in self.destinations]
        else:
            return [Signal(SignalType.HIGH, d, self.name) for d in self.destinations]


class Receiver:

    def __init__(self, name):
        self.name = name
        self.destinations = []

    def process(self, signal: Signal):
        if self.name == "rx" and signal.type == SignalType.LOW:
            print("COUCOU")

        return []


class Modules:

    def __init__(self):
        self.modules = {}

    def add_broadcaster(self, name, destinations):
        self.modules[name] = Broadcaster(name, destinations)

    def add_flipflop(self, name, destination):
        self.modules[name] = FlipFlop(name, destination)

    def add_conjunction(self, name, destination):
        self.modules[name] = Conjunction(name, destination)

    def add_receivers(self):
        receiver_names = []
        for module in self.modules.values():
            destinations = module.destinations
            for dest in destinations:
                if dest not in self.modules:
                    receiver_names.append(dest)
        for r in receiver_names:
            self.modules[r] = Receiver(r)

    def set_cunjunction_inputs(self):
        for module in self.modules.values():
            destinations = module.destinations
            for dest in destinations:
                dest_module = self.modules[dest]
                if type(dest_module) == Conjunction:
                    dest_module.add_input(module.name)

    def process(self, s: Signal):
        return self.modules[s.dest].process(s)


modules = Modules()

with open("input.txt") as file:
    for line in file:
        module_name, raw_dests = line.split("->")
        module_name = module_name.strip()
        dests = [d.strip() for d in raw_dests.split(",")]

        if module_name.strip() == "broadcaster":
            modules.add_broadcaster(module_name, dests)

        if module_name.startswith("%"):
            name = module_name[1:]
            modules.add_flipflop(name, dests)

        if module_name.startswith("&"):
            name = module_name[1:]
            modules.add_conjunction(name, dests)

modules.add_receivers()
modules.set_cunjunction_inputs()

for _ in range(1000000000):
    CYCLE += 1
    signals = [Signal(SignalType.LOW, "broadcaster", "button")]
    next_signals = []
    while signals:
        LOW_COUNT += sum(1 for s in signals if s.type == SignalType.LOW)
        HIGH_COUNT += sum(1 for s in signals if s.type == SignalType.HIGH)
        for s in signals:
            next_signals.extend(modules.process(s))
        signals.clear()
        signals.extend(next_signals)
        next_signals.clear()
print(LOW_COUNT)
print(HIGH_COUNT)
print(LOW_COUNT * HIGH_COUNT)
