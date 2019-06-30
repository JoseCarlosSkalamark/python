from ERROR import ERROR

class STR(str):
	def index_find(self, string="", start="left"):
		result = None
		if string not in self:
			ERROR("STR.index_find {string not found}")
		if start == "left":
			for char_position in range(len(self)):
				if self[char_position] == string:
					result = char_position
					break
		elif start == "right":
			for char_position in range(len(self)):
				if self[-char_position] == string:
					result = -char_position
					break
		else:
			ERROR("STR.index_find {parametro 'start' invalido}")
		return result
