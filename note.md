這個 project 的重點在於 使用 media query，CSS Grid 的概念去做 RWD，然後又再一次提到 html 用 if 去控制 class 屬性的方法，利用資料中的 slug 屬性去建立專案的獨立頁面，這個 project css 的篇幅蠻多的

flask 的 error handling

---

你好！

現在是將我們的應用程式部署到 Render.com 的時候了！這個過程與我們在第 8 節中所做的極其相似，所以這裡是一個快速回顧：

建立一個 requirements.txt 檔案（如果尚未），並將所有專案相依性新增至其中。不要忘記 pymongo[srv] 和 Gunicorn。

使用 MongoDB 連接字串建立 .env 文件，並從 app.py 文件載入環境變數。重要提示：請勿將 .env 檔案新增至 GitHub 儲存庫。

為您的專案建立 GitHub 儲存庫，並將專案檔案新增至其中。如果您手動新增文件，您將無法新增 .env 文件。那挺好的！

如果您使用 Git 新增文件，請先建立一個 .gitignore 文件並在其中寫入 .env。這將阻止 .env 檔案新增到您的 Git 儲存庫。

啟動 Render.com 並建立一個新的 Web 服務，將您的 GitHub 儲存庫連接到它。

在 Render.com 的環境標籤中，新增 MongoDB 連接字串，就像在 .env 檔案中一樣。
