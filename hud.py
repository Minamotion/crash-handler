import os, sys, pathlib, pyglet.font as pygletFont
import tkinter as tk, tkinter.font as tkFont


def path(path: pathlib.Path) -> pathlib.Path:
	return "{exepath}/{path}".format(exepath = os.path.dirname(__file__), path = path)


def get_datadir() -> pathlib.Path:
	if sys.platform.startswith("win"):
		return "%APPDATA%/Roaming"
	elif sys.platform.startswith("linux"):
		return "~/.local/share"
	elif sys.platform == "darwin":
		return "~/Library/Application Support"


def calculate_geometry(size: tuple[int, int], screen_size: tuple[int, int]) -> str:
	return "{w}x{h}+{x}+{y}".format(
		w = size[0],
		h = size[1],
		x = int((screen_size[0] /2) -(size[0] /2)),
		y = int((screen_size[1] /2) -(size[1] /2))
	)


def crash_window():
	#region [Set variables]
	text: dict[str, str]= {}
	with open(path("assets/data/text.csv"), "r") as file:
		for row in file.read().split("\n"):
			v = row.split(":")
			text[v[0]] = v[1].replace("\\n", "\n").replace("\\t", "\t")
		file.close()
	pygletFont.add_file(path("assets/fonts/pixel.ttf"))
	#endregion
	#region [Make tkinter window]
	root = tk.Tk()

	root.winfo_screenwidth()
	root.winfo_screenheight()

	bigfont = tkFont.Font(family="Pixel Arial 11", size=32)
	normalfont = tkFont.Font(family="Pixel Arial 11", size=8)

	root.title("Crash Handler - {title}".format(title = text["tkLabel_TITLE"]))
	root.minsize(750, 450)
	root.maxsize(750, 450)
	root.configure(bg = "white")
	root.geometry(calculate_geometry((750, 450), (root.winfo_screenwidth(), root.winfo_screenheight())))

	tk.Label(root, text = text["tkLabel_TITLE"], font = bigfont, bg = "white").pack()
	tk.Label(root, text = text["tkLabel_DESC"].format(appdata = get_datadir()), font = normalfont, bg = "white").pack()

	error__png = tk.PhotoImage(file = path("assets/images/error.png")).zoom(2)
	tk.Label(root, image = error__png, bg = "white").pack()

	root.mainloop()
	#endregion


if __name__ == '__main__':
	crash_window()