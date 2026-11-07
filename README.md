# 🌸 Café de Dreams – Virtual Café Ordering App

An aesthetic desktop virtual café ordering system built entirely in **Python with Tkinter**, inspired by Japanese Kawaii café POS dashboards, bakery interfaces, and modern minimalist tea shops.

---

## ✨ Features

- **Cute & Diverse Menu**:
  - ☕ **Brews & Lattes**: Caramel Ribbon Macchiato, Sakura Blossom Frappé, Vanilla Bean Cold Brew.
  - 🍵 **Matcha Magic**: Cloud Foam Matcha Latte, Uji Matcha Tiramisu.
  - 🧁 **Cute Cupcakes**: Galaxy Starlight Cupcake, Rose Berry Velvet Cupcake.
  - 🍪 **Cookies & Pastries**: Choco Lava Bunny Cookie, Teddy Bear Brioche, Pastel Rainbow Macarons.
  - 🍰 **Dream Cakes**: Strawberry Chiffon Cloud, White Peach Crepe Slice.
- **Interactive Menu Cards**:
  - Pastel visual containers with cute kawaii emojis and category badges (*Signature ⭐*, *Bestseller 🔥*, *Chef's Pick 🌸*, etc.).
  - Size selection (**Small**, **Regular**, **Large (+ $0.60)**) with real-time price updates.
  - Quantity steppers `[-]  qty  [+]`.
  - One-click *Add to Cart 🛒* button.
- **Search & Category Filters**:
  - Real-time search filter bar (type "matcha", "coffee", or "cookie").
  - Category pill filter buttons (*All Items*, *Brews*, *Matcha*, *Cupcakes*, *Pastries*, *Cakes*).
- **Today's Dream Combo Special**:
  - One-click combo special button (*Teddy Bear Brioche + Cloud Foam Matcha*).
- **Dining Preference Selection**:
  - 🍽️ **Dine-in (Table Service)**: Enables Table # input.
  - 🛍️ **Takeaway (Gift Bag & Box)**: Adds a +$0.50 packaging fee and sets table to To-Go.
- **Cute Add-ons & Extras**:
  - Extra whipped cream & sprinkles (+$0.50)
  - Cute gift box with satin ribbon (+$0.85)
  - Eco-friendly pastel cotton tote (+$0.45)
  - Extra espresso / ceremonial matcha shot (+$0.90)
- **Promo Coupon Codes**:
  - `DREAM10`: 10% discount off items
  - `SWEET2`: $2.00 off
  - `KAWAII`: $1.50 off
- **Live Bill Calculations**:
  - Subtotal, Add-ons & Packaging, Promo Discount, 8% Tax, and Grand Total calculated live.
- **Cute Order Confirmation Window**:
  - Generates a styled modal receipt with order number (`#CD-XXXX`), timestamp, customer details, itemized table, and cute mascot ASCII art:
    ```
       (\__/)
       (='.'=)  ♥ "Baked with fairy dust & love!"
       (")_(")     Estimated wait: 8 - 12 mins
    ```
  - **Save Receipt**: Exports formatted receipt to a `.txt` file via file dialog.
  - **New Order**: Clears cart and resets for the next guest.

---

## 🐍 Python Concepts Highlighted

| Concept | Implementation in Code |
| :--- | :--- |
| **Buttons (`tk.Button`)** | Category filter pills, quantity `[-]` and `[+]` steppers, `Add to Cart 🛒`, `Clear Search`, `Apply Coupon`, `💖 Place Order Now`, `🧹 Clear Tray`, `💾 Save Receipt`, `✨ Done / New Order`. |
| **Radio Buttons (`tk.Radiobutton`)** | Dining mode selection (`Dine-in` vs `Takeaway`), Serving size selection on each menu card (`S`, `M`, `L`). |
| **Checkboxes (`tk.Checkbutton`)** | Add-on extras (`Extra Whipped Cream`, `Gift Box & Ribbon`, `Eco Cotton Carrier`, `Extra Shot`). |
| **Labels (`tk.Label`)** | Brand header, subtitles, category tags, item titles, descriptions, dynamic prices, tray item count badges, receipt details, status bar. |
| **Calculations** | Real-time float math: unit price adjustments per size, subtotal calculation, add-ons summation, packaging fees, coupon percentage discounts, 8% sales tax, and grand total. |

---

## 🚀 How to Run

1. Open your terminal or Command Prompt.
2. Navigate to this folder:
   ```powershell
   cd C:\Users\kanik\.gemini\antigravity\scratch\cafe_de_dreams
   ```
3. Run the application with Python:
   ```powershell
   python app.py
   ```
   *(Or using the specific Python binary on your system)*:
   ```powershell
   & "C:\msys64\ucrt64\bin\python.exe" app.py
   ```

---

## 🎨 Color Palette & Aesthetic

- **Cream Canvas**: `#F8F5F0` (warm cozy off-white background)
- **Deep Mocha**: `#6C4A35` (header & primary brand identity)
- **Warm Caramel**: `#D48B55` (accent buttons & highlights)
- **Matcha Green**: `#7A9E7E` (tea accents & tags)
- **Strawberry Rose**: `#EAA4AC` (berry pastries & accents)
- **Roasted Coffee Dark**: `#3C281E` (crisp readable text)
