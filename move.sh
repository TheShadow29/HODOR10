for file in $( ls ~/Documents/ ); do
	if [ "$file" == "*.sprite2"]; then
		unzip $file;
		mkdir ~/Game/images/"$file"
		for i in $( ls ~/Documents/ ); do 
			if [ "$i" == "*.png"]; then
				mv $i ~/Game/images/"$file"/
			fi
		done
	fi
done
