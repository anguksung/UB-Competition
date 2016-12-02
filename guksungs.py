class Byte:
	
	def __init__(self, bits):
		'''bits is str or list of Number'''
		self.bits = []
		for bit in bits:
			if int(bit) in (0,1):
				self.bits.append(int(bit))
			else:
				raise ValueError

	def __add__(self, other):
		'''what about diff len?'''
		if len(self.bits) != len(other.bits): 
			raise ValueError('different size')
		from collections import deque
		bits = deque()
		carry = 0
		for upper, lower in reversed(list(zip(self.bits, other.bits))):
			bit = (upper + lower + carry) & 1
			# print(upper,lower,carry,'=',bit)
			bits.appendleft(bit)
			carry = (upper + lower + carry) >> 1

		if carry: raise OverflowError('overflow or underflow of bits')
		
		return Byte(bits)

	def to_2s_complement(self):
		if self.bits[0]:
			byte = self.flipped();
			byte += Byte('1')
			return byte
		return self

	def flipped(self):
		return Byte([bit ^ 1 for bit in self.bits])

	def bias_to_2s_complement(self):
		return Byte([self.bits[0] ^ 1] + self.bits[1:])

	def magnitude(self):
		negative = self.bits[0] * -2**(len(self.bits)-1)
		positives = (bit*2**i for i, bit in enumerate(self.bits[:0:-1]))
		return negative + sum(positives)

	def __str__(self):
		return ''.join([str(bit) for bit in self.bits])

bits1 = '100100'
bits2 = '001101'
b1 = Byte(bits1)
b2 = Byte(bits2)
one = Byte('1')

ss = input('what is ss')
print('ss', ss)

# w = b1 + one
# print('1 ^ 1 =', 1 ^ 1)
# print('0 ^ 1 =', 0 ^ 1)
# print()
# print(b1)
# print(b2)
# print('+')
# print(b1 + b2)
# print()
# print('magnitude')
# print(b1, '=', b1.magnitude())
# print(b2, '=', b2.magnitude())
# print()
# print('biased')
# print(b1.bias_to_2s_complement())
# print(b2.bias_to_2s_complement())