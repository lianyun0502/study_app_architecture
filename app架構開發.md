# MVVM 架構開發

Created: March 20, 2023 4:36 PM
Reviewed: No

## MVC

![Untitled](MVVM%20%E6%9E%B6%E6%A7%8B%E9%96%8B%E7%99%BC%2053f5165d2aed46b084a78208ffbd9972/Untitled.png)

View 與使用者直接互動，當 View 接收到使用者的回饋需要拿資料時(ex: 點擊下一頁的按鈕執行換頁)，呼叫 Controller，請 Controller 操作 Model 拿取想要的資料，Model 拿到資料後直接把資料丟回給 View，把資料顯示給使用者

- View負責記錄UI狀態和UI元件的交互，呼叫Controller事件
- Controller負責應用事件的邏輯，以及使用Models
- Model 領域模型負責做好該領域的需求，並要求View更新數據

**優點**

- 非常的直覺，好懂
- 使用 Controller 將 Model 和 View 分開來，具有一定程度的解耦合

**缺點**

- 三者相互依賴，一但更新了其中一者，另外兩者也必須跟著修改
- 隨著不斷的開發和添加功能，Controller 的代碼會越來越臃腫
- 難以進行單元測試

## MVP

![Untitled](MVVM%20%E6%9E%B6%E6%A7%8B%E9%96%8B%E7%99%BC%2053f5165d2aed46b084a78208ffbd9972/Untitled%201.png)

和 MVC 不同的是，Model 層拿到數據後，並不直接傳給 View 更新，而是交還給 Presenter，Presenter 再把數據交給 View，並更新畫面。

**優點**

- 從三者相互依賴變成都只依賴 Presenter (要改動的地方變少了)
- 責任分明，分工明確View 只負責收到使用者回饋後，呼叫 Presenter 拿取數據，並在接收到數據的時候，更新畫面。Model 被動的接收到 Presenter 命令，拿取資料，並回傳給 Presenter。Presenter 透過介面與 View 和 Model 溝通，是 View 和 Model 的唯一連結窗口。
- 方便進行單元測試　由於 Presenter 對 View 是透過介面進行操作，在對 Presenter 進行不依賴 UI 環境的單元測試的時候，可以 Mock 一個 View 對象，單元測試的時候就可以完整的測試 Presenter 業務邏輯的正確性。

**缺點**

- 隨著不斷的開發和添加功能，Presenter 的代碼會越來越臃腫

## MVVM

![Untitled](MVVM%20%E6%9E%B6%E6%A7%8B%E9%96%8B%E7%99%BC%2053f5165d2aed46b084a78208ffbd9972/Untitled%202.png)

![Untitled](MVVM%20%E6%9E%B6%E6%A7%8B%E9%96%8B%E7%99%BC%2053f5165d2aed46b084a78208ffbd9972/Untitled%203.png)

---

在 MVVM 架構裡面，**View 就是只有負責 UI 介面上的呈現或者純 UI 的邏輯**，這樣做是要讓職責更加明確，我們對於 View 只需要提供正確的資料，就能預期呈現正確的畫面和操作。

那麼介面上的資料處理和呈現邏輯該由誰負責呢？這就是 View Model 的職責，它擔任 View 和 Model 的橋樑，負責為 View 提供所需要呈現的資料以及操作互動提供對應的方法。

- View
    - UI畫面實作
    - 純UI邏輯
- View Model
    - 提供UI 資料流
    - 從Model取資料並做相應的轉換和處理邏輯後發送
    - View Model 裡不應該有UI的原件
- Model
    - 資料的來源，例如API、資料庫、Socket和檔案等等…
    - 對外提供資料的方式有很多，可以將Model封裝成觀察者模式，通知observer(view model)資料有改變。

## 實作 View Model

首先應該要先**明確需求**後寫出**抽象化介面**以及測試(實踐TDD開發)

## Clean architecture

![Source: [https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)](MVVM%20%E6%9E%B6%E6%A7%8B%E9%96%8B%E7%99%BC%2053f5165d2aed46b084a78208ffbd9972/Untitled%204.png)

Source: [https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

從程式架構來看，可以看到 View 使用 View Model，View Model 使用 Model，也就是依賴方向是 View → View Model → Model，View 知道 View Model 的存在，但 View Model 不知道 View 的存在，不曉得是哪一個 View 正在使用它。

這樣的概念曾在 [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) 提到，A → B 代表 A 依賴（使用） B，A 知道 B、B 不知道 A 的存在、B 不知道是誰在使用它。 這樣的設計是我們要確保元件之間有適當的隔離， B 受到保護不受到「A 的改變」而影響到或需要更動，也可以讓 A 可以延遲被決定（UI 擺放位置可以延遲到最後再決定）而不影響到 B。