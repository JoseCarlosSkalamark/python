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

	def index_find_multi_char(self, string="", start="left"):
		if string not in self:
			ERROR("STR.index_find_multi_char {string not found}")
		list_tmp = ["",[0]]
		if start == "left":
			for char_position in range(len(self)):
				if list_tmp[0] == string:
					break
				if self[char_position] == string[list_tmp[1][-1]]:
					list_tmp[0] += string[list_tmp[1][-1]]
					list_tmp[1].append(list_tmp[1][-1]+1)
			for i in list_tmp[1]:
				list_tmp[1][i] += self.index_find(string[0], start)
		elif start == "right":
			for char_position in range(len(self)):
				if list_tmp[0] == string:
					break
				if self[char_position] == string[list_tmp[1][-1]]:
					list_tmp[0] += string[list_tmp[1][-1]]
					list_tmp[1].append(list_tmp[1][-1]+1)
			for i in list_tmp[1]:
				list_tmp[1][i] += self.index_find(string[0], start)
		else:
			ERROR("STR.index_find_multi_char {parametro 'start' invalido}")
		return list_tmp
