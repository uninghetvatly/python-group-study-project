# =================================================================
# WEEK 8: OBJECT-ORIENTED PROGRAMMING (OOP) - COMPREHENSIVE
# =================================================================

# // Exercise 1: Class Definition with Class & Instance Attributes
# // Define a 'LogicGate' class to act as a base for digital components.
class LogicGate:
    # // Class Attribute: Shared by all gates
    technology = "CMOS" 

    def __init__(self, name, supply_voltage):
        # // Instance Attributes: Specific to each gate
        self.name = name
        self.vcc = supply_voltage
        # // Protected attribute: Intended for internal/subclass use
        self._is_active = False 
        # // Private attribute: Highly restricted
        self.__gate_id = "GATE-" + str(hash(name))[:5]

    # // Exercise 2: Instance Methods & Status Reporting
    def toggle_power(self):
        self._is_active = not self._is_active
        status = "ON" if self._is_active else "OFF"
        print(f"[{self.name}] Power toggled to {status}.")

    def get_info(self):
        return f"Gate: {self.name} | Tech: {self.technology} | VCC: {self.vcc}V"

# // Exercise 3: Inheritance & The super() Function
# // Create an 'ANDGate' that inherits from 'LogicGate'.
class ANDGate(LogicGate):
    def __init__(self, name, supply_voltage, input_count=2):
        # // Initialize the parent class attributes using super()
        super().__init__(name, supply_voltage)
        self.inputs = [0] * input_count

    # // Exercise 4: Functional Methods (The 'Behavior' of the object)
    # // Method to set inputs and calculate the output logic.
    def set_inputs(self, values):
        if len(values) != len(self.inputs):
            print(f"[ERROR] {self.name} requires exactly {len(self.inputs)} inputs.")
            return
        self.inputs = values
        print(f"[{self.name}] Inputs set to: {self.inputs}")

    def get_output(self):
        if not self._is_active:
            return "Error: Gate Power is OFF"
        # // Logic for AND gate: all inputs must be 1
        output = 1 if all(val == 1 for val in self.inputs) else 0
        return output

# // Exercise 5: Method Overriding
# // Demonstrate how a child class can change a parent's method behavior.
class NANDGate(ANDGate):
    def get_output(self):
        # // Override AND gate logic to perform NAND
        base_output = super().get_output()
        if isinstance(base_output, str): return base_output
        return 0 if base_output == 1 else 1

# -----------------------------------------------------------------
# EXECUTION AND TESTING
# -----------------------------------------------------------------

# // Creating Instances
gate1 = ANDGate("Main_AND", 3.3)
gate2 = NANDGate("Safety_NAND", 5.0)

print("--- System Initialization ---")
print(gate1.get_info())
print(gate2.get_info())

# // Testing Logic Flow
print("\n--- Logic Testing ---")
# // Trying to get output without power
print(f"Gate 1 Initial Output: {gate1.get_output()}") 

# // Powering on and setting inputs
gate1.toggle_power()
gate1.set_inputs([1, 1])
print(f"Gate 1 (1 AND 1) Result: {gate1.get_output()}")

# // Testing Inheritance and Overriding
gate2.toggle_power()
gate2.set_inputs([1, 1])
print(f"Gate 2 (1 NAND 1) Result: {gate2.get_output()}")

# // Exercise 6: Encapsulation Check
# // Trying to access private ID (This will fail or be difficult)
# // print(gate1.__gate_id) # -> AttributeError
print(f"\n[DEBUG] Internal Name (Mangled): {gate1._LogicGate__gate_id}")

# =================================================================
# END OF WEEK 8 PRACTICE
# =================================================================