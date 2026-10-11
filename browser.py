import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
from PyQt6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window title and size
        self.setWindowTitle("Obsidian")
        self.resize(1000, 700)

        # Create an in-memory (off-the-record) profile so no history or cache is saved to disk
        self.profile = QWebEngineProfile("PrivateProfile", self)
        self.profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.MemoryHttpCache)
        self.page = QWebEnginePage(self.profile, self)
        
        # The core web engine component using our private page
        self.browser = QWebEngineView()
        self.browser.setPage(self.page)
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Create a navigation toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Back Button
        back_btn = QPushButton("←")
        back_btn.clicked.connect(self.browser.back)
        toolbar.addWidget(back_btn)

        # Forward Button
        forward_btn = QPushButton("→")
        forward_btn.clicked.connect(self.browser.forward)
        toolbar.addWidget(forward_btn)

        # Reload Button
        reload_btn = QPushButton("⟳")
        reload_btn.clicked.connect(self.browser.reload)
        toolbar.addWidget(reload_btn)

        # URL / Address Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)

        # Update the address bar whenever the page URL changes
        self.browser.urlChanged.connect(self.update_url_bar)

        # Set up a central widget to hold the layout and browser view
        container = QWidget()
        container_layout = QVBoxLayout()
        container_layout.addWidget(toolbar)
        container_layout.addWidget(self.browser)
        
        # Remove default margins
        container_layout.setContentsMargins(0, 0, 0, 0)
        container.setLayout(container_layout)
        self.setCentralWidget(container)

    def navigate_to_url(self):
        """Loads the URL entered in the address bar."""
        url_text = self.url_bar.text()
        if not url_text.startswith("http://") and not url_text.startswith("https://"):
            url_text = "https://" + url_text
        self.browser.setUrl(QUrl(url_text))

    def update_url_bar(self, q):
        """Updates the text in the address bar to match the current webpage."""
        self.url_bar.setText(q.toString())

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())