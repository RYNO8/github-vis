function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

let checkBox = document.getElementById("toggle-box-checkbox");
checkBox.onclick = function() {
	let imgs = document.getElementsByTagName("img");
	console.log(imgs);
	if (checkBox.checked) {
		console.log("dark mode");
		setTheme('theme-dark');
		for (let i = 0; i < imgs.length; ++i) {
			if (imgs[i].src.indexOf("githubusercontent") == -1) {
				imgs[i].style.webkitFilter = "invert(100%)";
			}
		}
	}
	else  {
		console.log("light mode");
		setTheme('theme-light');
		for (let i = 0; i < imgs.length; ++i) {
			imgs[i].style.webkitFilter = "";
		}
	}
	console.log(imgs);
	
}
checkBox.onclick();