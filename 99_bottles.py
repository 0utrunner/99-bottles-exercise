def bottle_song(num):
	bottles = num
	while bottles > 1:
		removed = bottles - 1
		verse_1 = f'{bottles} bottles of beer on the wall! {bottles} bottles of beer!'
		verse_2 = f' Take one down and pass it around! {removed} bottles of beer on the wall!'
		verse_final = f'{bottles} bottles of beer on the wall! {bottles} bottles of beer! Take one down and pass it around! {removed} bottle of beer on the wall!'
		if bottles == 2:
			print(verse_final)
			bottles = bottles - 1
		else:
			print(verse_1 + verse_2)
			bottles = bottles - 1
		
	
	print(f'1 bottle of beer on the wall, 1 bottle of beer! Take one down and pass it around, no more bottles of beer on the wall! No more bottles of beer on the wall, no more bottles of beer! Go to the store and buy some more, {num} bottles of beer on the wall!!')
bottle_song(5)
