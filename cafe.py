"""
=============================================================================
  Café de Dreams – A Virtual Café Ordering App (Tkinter Frontend)
  ---------------------------------------------------------------------------
  A fictional aesthetic café ordering application with cute desserts & drinks!
  Inspired by modern Japanese/Kawaii café POS interfaces and bakery dashboards.

  Key Python Concepts Highlighted:
    1. Buttons (Category pills, quantity steppers, add-to-cart, checkout, etc.)
    2. Radio Buttons (Dine-in vs. Takeaway, item size selection: S, M, L)
    3. Checkboxes (Add-ons: whipped cream, gift box, tote bag, extra shots)
    4. Labels (Headers, badges, descriptions, dynamic prices, status bar)
    5. Calculations (Float math, subtotal, tax 8%, discounts, grand total)
=============================================================================
"""

import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import datetime

# Ensure stdout uses UTF-8 if running in terminal environments
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ---------------------------------------------------------------------------
# COLOR PALETTE (Warm Latte, Matcha, Strawberry & Cream Pastel Aesthetic)
# Reference: Wa Cafe POS, Coppie Cafe Dashboard & Kawaii Coffee Experience
# ---------------------------------------------------------------------------
THEME = {
    "bg_main": "#F8F5F0",         # Warm cream background
    "bg_surface": "#FFFFFF",      # Crisp white card/panel background
    "bg_subtle": "#F3EDE4",       # Soft warm beige for inputs & containers
    "bg_banner": "#FCEEE4",       # Peach-cream banner for Daily Special
    "bg_header": "#6C4A35",       # Deep mocha brown for primary navbar
    "header_sub": "#9C7A65",      # Warm coffee accent
    "accent_caramel": "#D48B55",  # Warm caramel CTA & badges
    "accent_pink": "#EAA4AC",     # Soft strawberry pink
    "accent_green": "#7A9E7E",    # Soft matcha green
    "accent_lavender": "#B8A7CE", # Pastel lavender
    "text_dark": "#3C281E",       # Deep roasted coffee dark text
    "text_muted": "#8A7568",      # Muted warm gray-brown for subtitles
    "border_light": "#EAE0D3",    # Subtle divider border
    "border_card": "#EDE5DC",     # Card border
    "price_green": "#467C59",     # Refreshing green for prices
    "danger_red": "#D9534F",      # Clear / remove accent
    "badge_bg": "#FDF2E9",        # Light peach badge
}

# ---------------------------------------------------------------------------
# MENU DATABASE (12 Handcrafted Cute Items)
# ---------------------------------------------------------------------------
MENU_ITEMS = [
    {
        "id": "item_1",
        "name": "Teddy Bear Brioche",
        "category": "Pastries",
        "desc": "Warm fluffy brioche bear filled with Belgian cocoa ganache.",
        "price": 4.80,
        "emoji": "🐻",
        "tag": "Signature ⭐",
        "bg_color": "#FDF0E2",
        "badge_color": "#D48B55"
    },
    {
        "id": "item_2",
        "name": "Cloud Foam Matcha Latte",
        "category": "Matcha",
        "desc": "Ceremonial Uji matcha topped with sweet cloud milk foam.",
        "price": 5.50,
        "emoji": "🍵",
        "tag": "Bestseller 🔥",
        "bg_color": "#EDF5EC",
        "badge_color": "#6E9572"
    },
    {
        "id": "item_3",
        "name": "Strawberry Chiffon Cloud",
        "category": "Cakes",
        "desc": "Japanese airy sponge cake with sweet strawberries & Hokkaido cream.",
        "price": 6.20,
        "emoji": "🍓",
        "tag": "Chef's Pick 🌸",
        "bg_color": "#FDECEF",
        "badge_color": "#D96B7D"
    },
    {
        "id": "item_4",
        "name": "Caramel Ribbon Macchiato",
        "category": "Coffee",
        "desc": "Double espresso, Madagascar vanilla syrup & warm caramel ribbon.",
        "price": 5.20,
        "emoji": "☕",
        "tag": "Popular ☕",
        "bg_color": "#F7EFE7",
        "badge_color": "#A06B49"
    },
    {
        "id": "item_5",
        "name": "Galaxy Starlight Cupcake",
        "category": "Cupcakes",
        "desc": "Velvet vanilla cupcake with purple galaxy swirl & edible stardust.",
        "price": 4.50,
        "emoji": "🌌",
        "tag": "Kawaii Special ✨",
        "bg_color": "#F4EFFB",
        "badge_color": "#9476C5"
    },
    {
        "id": "item_6",
        "name": "Uji Matcha Tiramisu",
        "category": "Matcha",
        "desc": "Velvety mascarpone, matcha soaked ladyfingers & emerald dust.",
        "price": 6.50,
        "emoji": "🍃",
        "tag": "Must Try 🌿",
        "bg_color": "#EDF5EC",
        "badge_color": "#6E9572"
    },
    {
        "id": "item_7",
        "name": "Choco Lava Bunny Cookie",
        "category": "Pastries",
        "desc": "Chewy sea-salt dark chocolate cookie with warm melting center.",
        "price": 3.80,
        "emoji": "🍪",
        "tag": "Freshly Baked ♨️",
        "bg_color": "#FDF0E2",
        "badge_color": "#D48B55"
    },
    {
        "id": "item_8",
        "name": "Sakura Blossom Frappé",
        "category": "Coffee",
        "desc": "Blended cherry blossom white chocolate milk with strawberry pearls.",
        "price": 5.90,
        "emoji": "🌸",
        "tag": "Seasonal 🌸",
        "bg_color": "#FDECEF",
        "badge_color": "#D96B7D"
    },
    {
        "id": "item_9",
        "name": "Pastel Rainbow Macaron Box",
        "category": "Pastries",
        "desc": "Trio of artisanal macarons: Rose Petal, Salted Butter, Pistachio.",
        "price": 5.40,
        "emoji": "🍬",
        "tag": "Sweet Treat 🍬",
        "bg_color": "#FDF0E2",
        "badge_color": "#D48B55"
    },
    {
        "id": "item_10",
        "name": "Rose Berry Velvet Cupcake",
        "category": "Cupcakes",
        "desc": "Rich raspberry cocoa sponge with silky whipped cream cheese rose.",
        "price": 4.90,
        "emoji": "🧁",
        "tag": "House Favorite 💖",
        "bg_color": "#FDECEF",
        "badge_color": "#D96B7D"
    },
    {
        "id": "item_11",
        "name": "White Peach Crepe Slice",
        "category": "Cakes",
        "desc": "20 delicate paper-thin crepes layered with white peach cream.",
        "price": 6.80,
        "emoji": "🍰",
        "tag": "Limited Edition 🍑",
        "bg_color": "#FBF0E9",
        "badge_color": "#DB8A63"
    },
    {
        "id": "item_12",
        "name": "Vanilla Bean Cold Brew",
        "category": "Coffee",
        "desc": "18-hour cold steeped coffee with French vanilla bean cold foam.",
        "price": 4.90,
        "emoji": "🧊",
        "tag": "Smooth & Bold ❄️",
        "bg_color": "#F7EFE7",
        "badge_color": "#A06B49"
    }
]

# ---------------------------------------------------------------------------
# ADD-ONS DEFINITION (Checkboxes Concept)
# ---------------------------------------------------------------------------
ADDONS_LIST = [
    ("extra_cream", "🍦 Extra Whipped Cream & Fairy Sprinkles", 0.50),
    ("gift_packaging", "🎁 Cute Gift Box & Pastel Satin Ribbon", 0.85),
    ("tote_bag", "🌸 Eco-Friendly Cotton Carry Carrier", 0.45),
    ("extra_shot", "☕ Extra Espresso / Ceremonial Matcha Shot", 0.90)
]

# ---------------------------------------------------------------------------
# MAIN APPLICATION CLASS
# ---------------------------------------------------------------------------
class CafeDeDreamsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Café de Dreams ☕ Virtual Ordering App")
        self.root.geometry("1280x830")
        self.root.minsize(1080, 720)
        self.root.configure(bg=THEME["bg_main"])

        # Typography configuration
        self.font_family = "Segoe UI"
        self.font_emoji = "Segoe UI Emoji"

        # Application State
        self.cart = {}  # key: (item_id, size), val: dict(item, size, unit_price, qty)
        self.selected_category = tk.StringVar(value="All")
        self.search_query = tk.StringVar(value="")
        self.customer_name = tk.StringVar(value="Dreamer")
        self.table_number = tk.StringVar(value="Table 04")
        self.dining_option = tk.StringVar(value="Dine-in")  # Python Concept: Radiobutton
        self.applied_discount = 0.0
        self.promo_code = tk.StringVar(value="")
        self.status_message = tk.StringVar(value="Welcome to Café de Dreams! Pick treats from the menu ✨")

        # Checkbox states (Python Concept: Checkbuttons)
        self.addon_vars = {}
        for key, name, price in ADDONS_LIST:
            self.addon_vars[key] = tk.BooleanVar(value=False)

        # Build Full UI Layout
        self.create_header()
        self.create_main_body()
        self.create_status_bar()

        # Initial Render
        self.filter_menu()
        self.update_cart_display()

    # -----------------------------------------------------------------------
    # TOP HEADER & LIVE SEARCH (Python Concept: Labels, Buttons)
    # -----------------------------------------------------------------------
    def create_header(self):
        header_frame = tk.Frame(self.root, bg=THEME["bg_header"], height=76)
        header_frame.pack(side=tk.TOP, fill=tk.X)
        header_frame.pack_propagate(False)

        # Brand / Logo Section (Left)
        brand_frame = tk.Frame(header_frame, bg=THEME["bg_header"])
        brand_frame.pack(side=tk.LEFT, padx=(24, 10), pady=10)

        # [PYTHON CONCEPT: Labels]
        logo_label = tk.Label(
            brand_frame,
            text="🌸 Café de Dreams",
            font=(self.font_family, 18, "bold"),
            fg="#FFFFFF",
            bg=THEME["bg_header"]
        )
        logo_label.pack(anchor="w")

        sub_label = tk.Label(
            brand_frame,
            text="A magical corner for specialty coffee, matcha & cute pastries ✨",
            font=(self.font_family, 9, "italic"),
            fg="#F1E4DA",
            bg=THEME["bg_header"]
        )
        sub_label.pack(anchor="w")

        # Live Search Bar (Right)
        search_frame = tk.Frame(header_frame, bg=THEME["bg_header"])
        search_frame.pack(side=tk.RIGHT, padx=24, pady=16)

        search_icon = tk.Label(
            search_frame,
            text="🔍",
            font=(self.font_emoji, 11),
            fg="#FFFFFF",
            bg=THEME["bg_header"]
        )
        search_icon.pack(side=tk.LEFT, padx=(0, 6))

        search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_query,
            font=(self.font_family, 10),
            bg="#FFFFFF",
            fg=THEME["text_dark"],
            relief=tk.FLAT,
            width=22,
            insertbackground=THEME["text_dark"]
        )
        search_entry.pack(side=tk.LEFT, ipady=4, padx=(0, 6))
        self.search_query.trace_add("write", lambda *args: self.filter_menu())

        # [PYTHON CONCEPT: Buttons]
        clear_btn = tk.Button(
            search_frame,
            text="Clear",
            font=(self.font_family, 8, "bold"),
            bg=THEME["accent_caramel"],
            fg="#FFFFFF",
            activebackground=THEME["header_sub"],
            activeforeground="#FFFFFF",
            relief=tk.FLAT,
            padx=10,
            pady=3,
            cursor="hand2",
            command=lambda: self.search_query.set("")
        )
        clear_btn.pack(side=tk.LEFT)

    # -----------------------------------------------------------------------
    # MAIN BODY: LEFT (MENU) & RIGHT (CART & CHECKOUT)
    # -----------------------------------------------------------------------
    def create_main_body(self):
        self.body_panes = tk.Frame(self.root, bg=THEME["bg_main"])
        self.body_panes.pack(fill=tk.BOTH, expand=True, padx=16, pady=(12, 6))

        # LEFT PANE: Menu Area (~68% width)
        self.menu_frame = tk.Frame(self.body_panes, bg=THEME["bg_main"])
        self.menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 12))

        # RIGHT PANE: Cart & Checkout (~32% width)
        self.cart_frame = tk.Frame(
            self.body_panes,
            bg=THEME["bg_surface"],
            width=440,
            highlightbackground=THEME["border_light"],
            highlightthickness=1
        )
        self.cart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(0, 0))
        self.cart_frame.pack_propagate(False)

        # Build Menu & Cart sub-sections
        self.build_category_bar()
        self.build_daily_special_banner()
        self.build_menu_grid_canvas()
        self.build_cart_panel()

    # -----------------------------------------------------------------------
    # CATEGORY FILTER PILL BUTTONS (Python Concept: Buttons)
    # -----------------------------------------------------------------------
    def build_category_bar(self):
        cat_bar = tk.Frame(self.menu_frame, bg=THEME["bg_main"])
        cat_bar.pack(side=tk.TOP, fill=tk.X, pady=(0, 8))

        categories = [
            ("All", "✨ All Items"),
            ("Coffee", "☕ Brews & Lattes"),
            ("Matcha", "🍵 Matcha Magic"),
            ("Cupcakes", "🧁 Cute Cupcakes"),
            ("Pastries", "🍪 Cookies & Brioche"),
            ("Cakes", "🍰 Dream Cakes")
        ]

        self.cat_buttons = {}
        for cat_key, cat_label in categories:
            # [PYTHON CONCEPT: Buttons]
            btn = tk.Button(
                cat_bar,
                text=cat_label,
                font=(self.font_family, 9, "bold"),
                relief=tk.FLAT,
                padx=12,
                pady=6,
                cursor="hand2",
                command=lambda k=cat_key: self.select_category(k)
            )
            btn.pack(side=tk.LEFT, padx=(0, 8))
            self.cat_buttons[cat_key] = btn

        self.update_category_buttons()

    def select_category(self, cat_key):
        self.selected_category.set(cat_key)
        self.update_category_buttons()
        self.filter_menu()

    def update_category_buttons(self):
        cur = self.selected_category.get()
        for key, btn in self.cat_buttons.items():
            if key == cur:
                btn.configure(
                    bg=THEME["bg_header"],
                    fg="#FFFFFF",
                    activebackground=THEME["bg_header"],
                    activeforeground="#FFFFFF"
                )
            else:
                btn.configure(
                    bg="#EAE0D3",
                    fg=THEME["text_dark"],
                    activebackground="#DFD4C5",
                    activeforeground=THEME["text_dark"]
                )

    # -----------------------------------------------------------------------
    # DAILY SPECIAL HERO BANNER (Inspired by Bunny Brew Cafe Reference)
    # -----------------------------------------------------------------------
    def build_daily_special_banner(self):
        banner = tk.Frame(
            self.menu_frame,
            bg=THEME["bg_banner"],
            highlightbackground=THEME["accent_caramel"],
            highlightthickness=1,
            padx=12,
            pady=8
        )
        banner.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))

        # Cute Mascot Icon
        tk.Label(
            banner,
            text="🐰",
            font=(self.font_emoji, 26),
            bg=THEME["bg_banner"]
        ).pack(side=tk.LEFT, padx=(4, 10))

        # Mascot Speech Text
        text_col = tk.Frame(banner, bg=THEME["bg_banner"])
        text_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(
            text_col,
            text="Today's Dream Combo Special! 🍵 + 🐻",
            font=(self.font_family, 9, "bold"),
            fg=THEME["text_dark"],
            bg=THEME["bg_banner"]
        ).pack(anchor="w")

        tk.Label(
            text_col,
            text="Cloud Foam Matcha Latte + Teddy Bear Brioche • Save $1.50 with coupon 'KAWAII'!",
            font=(self.font_family, 8),
            fg=THEME["text_muted"],
            bg=THEME["bg_banner"]
        ).pack(anchor="w")

        # One-Click Add Combo Button (Python Concept: Buttons)
        combo_btn = tk.Button(
            banner,
            text="+ Add Combo ($8.80) ✨",
            font=(self.font_family, 8, "bold"),
            bg=THEME["accent_caramel"],
            fg="#FFFFFF",
            relief=tk.FLAT,
            padx=10,
            pady=4,
            cursor="hand2",
            command=self.add_special_combo
        )
        combo_btn.pack(side=tk.RIGHT, padx=6)

    def add_special_combo(self):
        # Adds Matcha Latte + Teddy Brioche together
        self.add_item_to_cart(MENU_ITEMS[0], "Regular", 1)  # Teddy Bear Brioche
        self.add_item_to_cart(MENU_ITEMS[1], "Regular", 1)  # Cloud Foam Matcha
        self.status_message.set("🎉 Added Today's Dream Combo (Teddy Brioche + Cloud Matcha) to your tray!")

    # -----------------------------------------------------------------------
    # SCROLLABLE MENU CARDS GRID
    # -----------------------------------------------------------------------
    def build_menu_grid_canvas(self):
        grid_container = tk.Frame(self.menu_frame, bg=THEME["bg_main"])
        grid_container.pack(fill=tk.BOTH, expand=True)

        self.menu_canvas = tk.Canvas(
            grid_container,
            bg=THEME["bg_main"],
            highlightthickness=0
        )
        self.menu_scrollbar = ttk.Scrollbar(
            grid_container,
            orient=tk.VERTICAL,
            command=self.menu_canvas.yview
        )

        self.cards_inner_frame = tk.Frame(self.menu_canvas, bg=THEME["bg_main"])
        self.cards_inner_frame.bind(
            "<Configure>",
            lambda e: self.menu_canvas.configure(scrollregion=self.menu_canvas.bbox("all"))
        )

        self.menu_canvas_window = self.menu_canvas.create_window(
            (0, 0),
            window=self.cards_inner_frame,
            anchor="nw"
        )

        self.menu_canvas.configure(yscrollcommand=self.menu_scrollbar.set)
        self.menu_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.menu_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Smooth Mousewheel scrolling
        self.menu_canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.menu_canvas.bind(
            "<Configure>",
            lambda e: self.menu_canvas.itemconfig(self.menu_canvas_window, width=e.width)
        )

    def _on_mousewheel(self, event):
        try:
            self.menu_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        except Exception:
            pass

    # -----------------------------------------------------------------------
    # FILTER AND RENDER MENU CARDS
    # -----------------------------------------------------------------------
    def filter_menu(self):
        for widget in self.cards_inner_frame.winfo_children():
            widget.destroy()

        cat = self.selected_category.get()
        query = self.search_query.get().strip().lower()

        filtered = []
        for item in MENU_ITEMS:
            match_cat = (cat == "All") or (item["category"] == cat)
            match_q = (not query) or (query in item["name"].lower()) or (query in item["desc"].lower())
            if match_cat and match_q:
                filtered.append(item)

        if not filtered:
            empty_msg = tk.Label(
                self.cards_inner_frame,
                text="🍃 No dreamy treats found!\nTry searching for something else or pick 'All Items'.",
                font=(self.font_family, 12, "italic"),
                fg=THEME["text_muted"],
                bg=THEME["bg_main"],
                pady=60
            )
            empty_msg.pack(fill=tk.BOTH, expand=True)
            return

        # 2-column responsive layout
        cols = 2
        for idx, item in enumerate(filtered):
            r = idx // cols
            c = idx % cols
            card = self.create_item_card(self.cards_inner_frame, item)
            card.grid(row=r, column=c, padx=8, pady=8, sticky="nsew")

        for c_idx in range(cols):
            self.cards_inner_frame.columnconfigure(c_idx, weight=1)

    # -----------------------------------------------------------------------
    # SINGLE ITEM CARD CREATION
    # Highlights: Buttons, Radio Buttons, Labels, Calculations
    # -----------------------------------------------------------------------
    def create_item_card(self, parent, item):
        card = tk.Frame(
            parent,
            bg=THEME["bg_surface"],
            highlightbackground=THEME["border_card"],
            highlightthickness=1,
            padx=12,
            pady=12
        )

        # Header Visual Container: Pastel background with Emoji & Tag badge
        vis_frame = tk.Frame(card, bg=item["bg_color"], height=88)
        vis_frame.pack(fill=tk.X, pady=(0, 8))
        vis_frame.pack_propagate(False)

        # [PYTHON CONCEPT: Labels] Tag Badge
        badge_lbl = tk.Label(
            vis_frame,
            text=item["tag"],
            font=(self.font_family, 8, "bold"),
            fg="#FFFFFF",
            bg=item["badge_color"],
            padx=7,
            pady=2
        )
        badge_lbl.pack(anchor="ne", padx=6, pady=6)

        # [PYTHON CONCEPT: Labels] Center Kawaii Emoji
        emoji_lbl = tk.Label(
            vis_frame,
            text=item["emoji"],
            font=(self.font_emoji, 34),
            bg=item["bg_color"]
        )
        emoji_lbl.place(relx=0.5, rely=0.52, anchor="center")

        # [PYTHON CONCEPT: Labels] Title & Description
        title_lbl = tk.Label(
            card,
            text=item["name"],
            font=(self.font_family, 11, "bold"),
            fg=THEME["text_dark"],
            bg=THEME["bg_surface"],
            anchor="w"
        )
        title_lbl.pack(fill=tk.X)

        desc_lbl = tk.Label(
            card,
            text=item["desc"],
            font=(self.font_family, 8),
            fg=THEME["text_muted"],
            bg=THEME["bg_surface"],
            wraplength=220,
            justify="left",
            anchor="w"
        )
        desc_lbl.pack(fill=tk.X, pady=(2, 6))

        # [PYTHON CONCEPT: Radio Buttons] Size Selection
        size_frame = tk.Frame(card, bg=THEME["bg_surface"])
        size_frame.pack(fill=tk.X, pady=(0, 6))

        size_var = tk.StringVar(value="Regular")

        size_lbl = tk.Label(
            size_frame,
            text="Size:",
            font=(self.font_family, 8, "bold"),
            fg=THEME["text_muted"],
            bg=THEME["bg_surface"]
        )
        size_lbl.pack(side=tk.LEFT, padx=(0, 4))

        # Dynamic Price Label
        bottom_frame = tk.Frame(card, bg=THEME["bg_surface"])
        bottom_frame.pack(fill=tk.X, pady=(4, 0))

        # [PYTHON CONCEPT: Calculations & Labels]
        price_lbl = tk.Label(
            bottom_frame,
            text=f"${item['price']:.2f}",
            font=(self.font_family, 12, "bold"),
            fg=THEME["price_green"],
            bg=THEME["bg_surface"]
        )
        price_lbl.pack(side=tk.LEFT)

        def on_size_changed():
            # [PYTHON CONCEPT: Calculations] Update price label on size radio selection
            chosen_size = size_var.get()
            extra = 0.60 if chosen_size == "Large" else 0.0
            new_price = item["price"] + extra
            price_lbl.configure(text=f"${new_price:.2f}")

        sizes = [("S", "Small"), ("M", "Regular"), ("L", "Large (+0.60)")]
        for s_code, s_name in sizes:
            # [PYTHON CONCEPT: Radio Buttons]
            rb = tk.Radiobutton(
                size_frame,
                text=s_code,
                value=s_name,
                variable=size_var,
                font=(self.font_family, 8),
                bg=THEME["bg_surface"],
                fg=THEME["text_dark"],
                activebackground=THEME["bg_surface"],
                selectcolor="#F7EBE1",
                cursor="hand2",
                command=on_size_changed
            )
            rb.pack(side=tk.LEFT, padx=2)

        # Quantity Stepper controls
        qty_var = tk.IntVar(value=1)
        stepper_frame = tk.Frame(bottom_frame, bg=THEME["bg_subtle"])
        stepper_frame.pack(side=tk.RIGHT)

        # [PYTHON CONCEPT: Buttons]
        minus_btn = tk.Button(
            stepper_frame,
            text="-",
            font=(self.font_family, 8, "bold"),
            bg="#EAE0D3",
            fg=THEME["text_dark"],
            relief=tk.FLAT,
            width=2,
            cursor="hand2",
            command=lambda: self.adjust_card_qty(qty_var, -1)
        )
        minus_btn.pack(side=tk.LEFT)

        # [PYTHON CONCEPT: Labels]
        qty_display = tk.Label(
            stepper_frame,
            textvariable=qty_var,
            font=(self.font_family, 9, "bold"),
            bg=THEME["bg_subtle"],
            fg=THEME["text_dark"],
            width=2
        )
        qty_display.pack(side=tk.LEFT, padx=3)

        # [PYTHON CONCEPT: Buttons]
        plus_btn = tk.Button(
            stepper_frame,
            text="+",
            font=(self.font_family, 8, "bold"),
            bg="#EAE0D3",
            fg=THEME["text_dark"],
            relief=tk.FLAT,
            width=2,
            cursor="hand2",
            command=lambda: self.adjust_card_qty(qty_var, 1)
        )
        plus_btn.pack(side=tk.LEFT)

        # [PYTHON CONCEPT: Buttons] Primary Add to Cart Button
        add_btn = tk.Button(
            card,
            text="Add to Cart 🛒",
            font=(self.font_family, 9, "bold"),
            bg=THEME["accent_caramel"],
            fg="#FFFFFF",
            activebackground=THEME["header_sub"],
            activeforeground="#FFFFFF",
            relief=tk.FLAT,
            pady=5,
            cursor="hand2",
            command=lambda: self.add_item_to_cart(item, size_var.get(), qty_var.get())
        )
        add_btn.pack(fill=tk.X, pady=(8, 0))

        return card

    def adjust_card_qty(self, qty_var, delta):
        cur = qty_var.get()
        new_val = max(1, cur + delta)
        qty_var.set(new_val)

    # -----------------------------------------------------------------------
    # RIGHT PANE: CART & BILLING PANEL
    # Demonstrating: Radio buttons, Checkboxes, Buttons, Labels, Calculations
    # -----------------------------------------------------------------------
    def build_cart_panel(self):
        # 1. Top Cart Header
        cart_head = tk.Frame(self.cart_frame, bg=THEME["bg_subtle"], height=52)
        cart_head.pack(side=tk.TOP, fill=tk.X)
        cart_head.pack_propagate(False)

        # [PYTHON CONCEPT: Labels]
        cart_title = tk.Label(
            cart_head,
            text="✨ Your Dream Tray",
            font=(self.font_family, 12, "bold"),
            fg=THEME["text_dark"],
            bg=THEME["bg_subtle"]
        )
        cart_title.pack(side=tk.LEFT, padx=14, pady=12)

        # [PYTHON CONCEPT: Labels] Badge Count
        self.cart_count_badge = tk.Label(
            cart_head,
            text="0 items",
            font=(self.font_family, 9, "bold"),
            fg="#FFFFFF",
            bg=THEME["accent_caramel"],
            padx=8,
            pady=2
        )
        self.cart_count_badge.pack(side=tk.RIGHT, padx=14)

        # 2. Customer & Dining Option (Python Concept: Radio Buttons)
        dining_frame = tk.LabelFrame(
            self.cart_frame,
            text=" 🏷️ Dining Preference ",
            font=(self.font_family, 8, "bold"),
            fg=THEME["text_muted"],
            bg=THEME["bg_surface"],
            padx=10,
            pady=6
        )
        dining_frame.pack(fill=tk.X, padx=12, pady=(8, 4))

        # [PYTHON CONCEPT: Radio Buttons] Select takeaway or dine-in
        rb_dine = tk.Radiobutton(
            dining_frame,
            text="🍽️ Dine-in (Table Service)",
            value="Dine-in",
            variable=self.dining_option,
            font=(self.font_family, 9),
            bg=THEME["bg_surface"],
            fg=THEME["text_dark"],
            selectcolor="#F7EBE1",
            activebackground=THEME["bg_surface"],
            cursor="hand2",
            command=self.on_dining_option_changed
        )
        rb_dine.pack(side=tk.LEFT, padx=(0, 10))

        rb_takeaway = tk.Radiobutton(
            dining_frame,
            text="🛍️ Takeaway (+ $0.50)",
            value="Takeaway",
            variable=self.dining_option,
            font=(self.font_family, 9),
            bg=THEME["bg_surface"],
            fg=THEME["text_dark"],
            selectcolor="#F7EBE1",
            activebackground=THEME["bg_surface"],
            cursor="hand2",
            command=self.on_dining_option_changed
        )
        rb_takeaway.pack(side=tk.LEFT)

        # Customer Name & Table Number fields
        details_frame = tk.Frame(self.cart_frame, bg=THEME["bg_surface"])
        details_frame.pack(fill=tk.X, padx=12, pady=(2, 6))

        tk.Label(
            details_frame,
            text="Name:",
            font=(self.font_family, 8),
            fg=THEME["text_muted"],
            bg=THEME["bg_surface"]
        ).pack(side=tk.LEFT)

        cust_entry = tk.Entry(
            details_frame,
            textvariable=self.customer_name,
            font=(self.font_family, 8),
            bg=THEME["bg_subtle"],
            fg=THEME["text_dark"],
            relief=tk.FLAT,
            width=14
        )
        cust_entry.pack(side=tk.LEFT, padx=(4, 10))

        tk.Label(
            details_frame,
            text="Table #:",
            font=(self.font_family, 8),
            fg=THEME["text_muted"],
            bg=THEME["bg_surface"]
        ).pack(side=tk.LEFT)

        self.table_entry = tk.Entry(
            details_frame,
            textvariable=self.table_number,
            font=(self.font_family, 8),
            bg=THEME["bg_subtle"],
            fg=THEME["text_dark"],
            relief=tk.FLAT,
            width=10
        )
        self.table_entry.pack(side=tk.LEFT, padx=4)

        # 3. Scrollable List of Cart Items
        cart_list_container = tk.Frame(self.cart_frame, bg=THEME["bg_surface"])
        cart_list_container.pack(fill=tk.BOTH, expand=True, padx=12, pady=4)

        self.cart_canvas = tk.Canvas(
            cart_list_container,
            bg=THEME["bg_surface"],
            highlightthickness=0
        )
        self.cart_scrollbar = ttk.Scrollbar(
            cart_list_container,
            orient=tk.VERTICAL,
            command=self.cart_canvas.yview
        )

        self.cart_items_inner = tk.Frame(self.cart_canvas, bg=THEME["bg_surface"])
        self.cart_items_inner.bind(
            "<Configure>",
            lambda e: self.cart_canvas.configure(scrollregion=self.cart_canvas.bbox("all"))
        )

        self.cart_canvas_window = self.cart_canvas.create_window(
            (0, 0),
            window=self.cart_items_inner,
            anchor="nw"
        )

        self.cart_canvas.configure(yscrollcommand=self.cart_scrollbar.set)
        self.cart_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.cart_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.cart_canvas.bind(
            "<Configure>",
            lambda e: self.cart_canvas.itemconfig(self.cart_canvas_window, width=e.width)
        )

        # 4. Cute Add-ons Section (Python Concept: Checkboxes)
        addons_frame = tk.LabelFrame(
            self.cart_frame,
            text=" 🎀 Dreamy Add-ons & Extras ",
            font=(self.font_family, 8, "bold"),
            fg=THEME["text_muted"],
            bg=THEME["bg_surface"],
            padx=10,
            pady=4
        )
        addons_frame.pack(fill=tk.X, padx=12, pady=(4, 4))

        # [PYTHON CONCEPT: Checkboxes]
        for key, name, price in ADDONS_LIST:
            cb = tk.Checkbutton(
                addons_frame,
                text=f"{name} (+${price:.2f})",
                variable=self.addon_vars[key],
                font=(self.font_family, 8),
                bg=THEME["bg_surface"],
                fg=THEME["text_dark"],
                selectcolor="#F7EBE1",
                activebackground=THEME["bg_surface"],
                cursor="hand2",
                command=self.update_bill_calculations
            )
            cb.pack(anchor="w", pady=1)

        # 5. Promo Voucher Code Section (Python Concept: Entry, Buttons)
        promo_frame = tk.Frame(self.cart_frame, bg=THEME["bg_surface"])
        promo_frame.pack(fill=tk.X, padx=12, pady=(2, 4))

        promo_entry = tk.Entry(
            promo_frame,
            textvariable=self.promo_code,
            font=(self.font_family, 8),
            bg=THEME["bg_subtle"],
            fg=THEME["text_dark"],
            relief=tk.FLAT,
            width=18
        )
        promo_entry.pack(side=tk.LEFT, ipady=2, padx=(0, 6))

        # [PYTHON CONCEPT: Buttons]
        apply_btn = tk.Button(
            promo_frame,
            text="Apply Coupon",
            font=(self.font_family, 8, "bold"),
            bg="#EAE0D3",
            fg=THEME["text_dark"],
            relief=tk.FLAT,
            cursor="hand2",
            padx=8,
            command=self.apply_promo_coupon
        )
        apply_btn.pack(side=tk.LEFT)

        # 6. Bill Summary & Calculations Area (Python Concept: Labels & Calculations)
        summary_frame = tk.Frame(
            self.cart_frame,
            bg=THEME["bg_subtle"],
            padx=12,
            pady=8
        )
        summary_frame.pack(fill=tk.X, padx=12, pady=(4, 6))

        # Subtotal Row
        r1 = tk.Frame(summary_frame, bg=THEME["bg_subtle"])
        r1.pack(fill=tk.X, pady=1)
        tk.Label(r1, text="Items Subtotal:", font=(self.font_family, 8), fg=THEME["text_muted"], bg=THEME["bg_subtle"]).pack(side=tk.LEFT)
        self.lbl_subtotal = tk.Label(r1, text="$0.00", font=(self.font_family, 8, "bold"), fg=THEME["text_dark"], bg=THEME["bg_subtle"])
        self.lbl_subtotal.pack(side=tk.RIGHT)

        # Addons & Packaging Row
        r2 = tk.Frame(summary_frame, bg=THEME["bg_subtle"])
        r2.pack(fill=tk.X, pady=1)
        tk.Label(r2, text="Add-ons & Packaging:", font=(self.font_family, 8), fg=THEME["text_muted"], bg=THEME["bg_subtle"]).pack(side=tk.LEFT)
        self.lbl_addons = tk.Label(r2, text="$0.00", font=(self.font_family, 8), fg=THEME["text_dark"], bg=THEME["bg_subtle"])
        self.lbl_addons.pack(side=tk.RIGHT)

        # Tax Row
        r3 = tk.Frame(summary_frame, bg=THEME["bg_subtle"])
        r3.pack(fill=tk.X, pady=1)
        tk.Label(r3, text="Estimated Tax (8%):", font=(self.font_family, 8), fg=THEME["text_muted"], bg=THEME["bg_subtle"]).pack(side=tk.LEFT)
        self.lbl_tax = tk.Label(r3, text="$0.00", font=(self.font_family, 8), fg=THEME["text_dark"], bg=THEME["bg_subtle"])
        self.lbl_tax.pack(side=tk.RIGHT)

        # Discount Row
        self.r_disc = tk.Frame(summary_frame, bg=THEME["bg_subtle"])
        self.r_disc.pack(fill=tk.X, pady=1)
        tk.Label(self.r_disc, text="Promo Discount:", font=(self.font_family, 8), fg=THEME["price_green"], bg=THEME["bg_subtle"]).pack(side=tk.LEFT)
        self.lbl_discount = tk.Label(self.r_disc, text="-$0.00", font=(self.font_family, 8, "bold"), fg=THEME["price_green"], bg=THEME["bg_subtle"])
        self.lbl_discount.pack(side=tk.RIGHT)

        # Divider line
        tk.Frame(summary_frame, bg=THEME["border_light"], height=1).pack(fill=tk.X, pady=4)

        # Grand Total Row
        r_tot = tk.Frame(summary_frame, bg=THEME["bg_subtle"])
        r_tot.pack(fill=tk.X, pady=1)
        tk.Label(r_tot, text="Grand Total:", font=(self.font_family, 11, "bold"), fg=THEME["text_dark"], bg=THEME["bg_subtle"]).pack(side=tk.LEFT)
        self.lbl_total = tk.Label(r_tot, text="$0.00", font=(self.font_family, 13, "bold"), fg=THEME["accent_caramel"], bg=THEME["bg_subtle"])
        self.lbl_total.pack(side=tk.RIGHT)

        # 7. Action Buttons (Place Order & Clear Tray)
        action_frame = tk.Frame(self.cart_frame, bg=THEME["bg_surface"])
        action_frame.pack(fill=tk.X, padx=12, pady=(4, 12))

        # [PYTHON CONCEPT: Buttons]
        self.btn_order = tk.Button(
            action_frame,
            text="💖 Place Order Now",
            font=(self.font_family, 10, "bold"),
            bg=THEME["accent_caramel"],
            fg="#FFFFFF",
            activebackground=THEME["header_sub"],
            activeforeground="#FFFFFF",
            relief=tk.FLAT,
            pady=7,
            cursor="hand2",
            command=self.confirm_and_place_order
        )
        self.btn_order.pack(fill=tk.X, pady=(0, 4))

        # [PYTHON CONCEPT: Buttons]
        btn_clear = tk.Button(
            action_frame,
            text="🧹 Clear Tray",
            font=(self.font_family, 8),
            bg=THEME["bg_surface"],
            fg=THEME["text_muted"],
            activebackground=THEME["bg_subtle"],
            activeforeground=THEME["danger_red"],
            relief=tk.FLAT,
            cursor="hand2",
            command=self.clear_cart
        )
        btn_clear.pack(fill=tk.X)

    def on_dining_option_changed(self):
        # Update Table Entry state based on radio selection
        if self.dining_option.get() == "Takeaway":
            self.table_entry.configure(state=tk.DISABLED)
            self.table_number.set("To-Go Bag")
        else:
            self.table_entry.configure(state=tk.NORMAL)
            if self.table_number.get() == "To-Go Bag":
                self.table_number.set("Table 04")
        self.update_bill_calculations()

    # -----------------------------------------------------------------------
    # STATUS BAR
    # -----------------------------------------------------------------------
    def create_status_bar(self):
        status_bar = tk.Frame(self.root, bg="#ECE5DA", height=24)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # [PYTHON CONCEPT: Labels]
        status_lbl = tk.Label(
            status_bar,
            textvariable=self.status_message,
            font=(self.font_family, 8),
            fg=THEME["text_muted"],
            bg="#ECE5DA",
            padx=12
        )
        status_lbl.pack(side=tk.LEFT)

        tip_lbl = tk.Label(
            status_bar,
            text="Coupons available: 'DREAM10' (10% off) | 'SWEET2' ($2 off) | 'KAWAII' ($1.50 off) ✨",
            font=(self.font_family, 8, "italic"),
            fg=THEME["text_muted"],
            bg="#ECE5DA",
            padx=12
        )
        tip_lbl.pack(side=tk.RIGHT)

    # -----------------------------------------------------------------------
    # CART ACTIONS & LIVE CALCULATIONS
    # -----------------------------------------------------------------------
    def add_item_to_cart(self, item, size, qty):
        size_diff = 0.60 if "Large" in size else 0.0
        unit_price = item["price"] + size_diff

        key = (item["id"], size)
        if key in self.cart:
            self.cart[key]["qty"] += qty
        else:
            self.cart[key] = {
                "item": item,
                "size": size,
                "unit_price": unit_price,
                "qty": qty
            }

        self.status_message.set(f"✨ Added {qty}x {item['name']} ({size}) to your tray!")
        self.update_cart_display()

    def update_cart_display(self):
        for widget in self.cart_items_inner.winfo_children():
            widget.destroy()

        if not self.cart:
            empty_lbl = tk.Label(
                self.cart_items_inner,
                text="🧁 Your tray is empty!\nSelect some cute treats to start.",
                font=(self.font_family, 9, "italic"),
                fg=THEME["text_muted"],
                bg=THEME["bg_surface"],
                pady=30
            )
            empty_lbl.pack(fill=tk.BOTH, expand=True)
            self.cart_count_badge.configure(text="0 items")
            self.btn_order.configure(state=tk.DISABLED, bg="#D9CBC0")
        else:
            total_items_count = sum(entry["qty"] for entry in self.cart.values())
            self.cart_count_badge.configure(text=f"{total_items_count} item{'s' if total_items_count > 1 else ''}")
            self.btn_order.configure(state=tk.NORMAL, bg=THEME["accent_caramel"])

            for key, entry in self.cart.items():
                self.render_cart_item_row(key, entry)

        self.update_bill_calculations()

    def render_cart_item_row(self, key, entry):
        item = entry["item"]
        size = entry["size"]
        qty = entry["qty"]
        line_total = entry["unit_price"] * qty

        row = tk.Frame(
            self.cart_items_inner,
            bg=THEME["bg_subtle"],
            highlightbackground=THEME["border_light"],
            highlightthickness=1,
            padx=8,
            pady=6
        )
        row.pack(fill=tk.X, pady=3)

        # Emoji thumbnail
        tk.Label(
            row,
            text=item["emoji"],
            font=(self.font_emoji, 14),
            bg=THEME["bg_subtle"]
        ).pack(side=tk.LEFT, padx=(0, 6))

        # Title & Size description
        info_col = tk.Frame(row, bg=THEME["bg_subtle"])
        info_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(
            info_col,
            text=item["name"],
            font=(self.font_family, 8, "bold"),
            fg=THEME["text_dark"],
            bg=THEME["bg_subtle"],
            anchor="w"
        ).pack(fill=tk.X)

        tk.Label(
            info_col,
            text=f"Size: {size} • ${entry['unit_price']:.2f} ea",
            font=(self.font_family, 7),
            fg=THEME["text_muted"],
            bg=THEME["bg_subtle"],
            anchor="w"
        ).pack(fill=tk.X)

        # Stepper Buttons
        stepper = tk.Frame(row, bg=THEME["bg_subtle"])
        stepper.pack(side=tk.LEFT, padx=6)

        minus_btn = tk.Button(
            stepper,
            text="-",
            font=(self.font_family, 7, "bold"),
            bg="#E2D6C7",
            relief=tk.FLAT,
            width=2,
            cursor="hand2",
            command=lambda: self.change_cart_item_qty(key, -1)
        )
        minus_btn.pack(side=tk.LEFT)

        tk.Label(
            stepper,
            text=str(qty),
            font=(self.font_family, 8, "bold"),
            bg=THEME["bg_subtle"],
            fg=THEME["text_dark"],
            width=2
        ).pack(side=tk.LEFT)

        plus_btn = tk.Button(
            stepper,
            text="+",
            font=(self.font_family, 7, "bold"),
            bg="#E2D6C7",
            relief=tk.FLAT,
            width=2,
            cursor="hand2",
            command=lambda: self.change_cart_item_qty(key, 1)
        )
        plus_btn.pack(side=tk.LEFT)

        # Line total price
        tk.Label(
            row,
            text=f"${line_total:.2f}",
            font=(self.font_family, 8, "bold"),
            fg=THEME["price_green"],
            bg=THEME["bg_subtle"],
            width=6,
            anchor="e"
        ).pack(side=tk.LEFT, padx=2)

        # Delete (✕) button
        del_btn = tk.Button(
            row,
            text="✕",
            font=(self.font_family, 7, "bold"),
            bg=THEME["bg_subtle"],
            fg=THEME["danger_red"],
            activebackground=THEME["bg_subtle"],
            activeforeground="#990000",
            relief=tk.FLAT,
            cursor="hand2",
            command=lambda: self.remove_cart_item(key)
        )
        del_btn.pack(side=tk.RIGHT, padx=(4, 0))

    def change_cart_item_qty(self, key, delta):
        if key in self.cart:
            self.cart[key]["qty"] += delta
            if self.cart[key]["qty"] <= 0:
                del self.cart[key]
            self.update_cart_display()

    def remove_cart_item(self, key):
        if key in self.cart:
            del self.cart[key]
            self.update_cart_display()

    def clear_cart(self):
        if not self.cart:
            return
        if messagebox.askyesno("Clear Tray", "Are you sure you want to clear your current tray?"):
            self.cart.clear()
            self.applied_discount = 0.0
            self.update_cart_display()
            self.status_message.set("Tray cleared. Ready for fresh choices! ✨")

    # -----------------------------------------------------------------------
    # PROMO COUPON CODE
    # -----------------------------------------------------------------------
    def apply_promo_coupon(self):
        code = self.promo_code.get().strip().upper()
        if not self.cart:
            messagebox.showinfo("Coupon", "Please add some items to your tray first!")
            return

        items_subtotal = sum(entry["unit_price"] * entry["qty"] for entry in self.cart.values())

        # [PYTHON CONCEPT: Calculations]
        if code == "DREAM10":
            self.applied_discount = items_subtotal * 0.10
            self.status_message.set("🎉 Coupon 'DREAM10' applied! 10% discount.")
            messagebox.showinfo("Success", "Coupon 'DREAM10' applied! You got 10% off.")
        elif code == "SWEET2":
            self.applied_discount = min(2.00, items_subtotal)
            self.status_message.set("🎉 Coupon 'SWEET2' applied! $2.00 discount.")
            messagebox.showinfo("Success", "Coupon 'SWEET2' applied! You got $2.00 off.")
        elif code == "KAWAII":
            self.applied_discount = min(1.50, items_subtotal)
            self.status_message.set("🎉 Coupon 'KAWAII' applied! $1.50 discount.")
            messagebox.showinfo("Success", "Coupon 'KAWAII' applied! You got $1.50 off.")
        else:
            self.applied_discount = 0.0
            messagebox.showwarning("Invalid Coupon", "Valid codes: DREAM10, SWEET2, KAWAII")

        self.update_bill_calculations()

    # -----------------------------------------------------------------------
    # BILL CALCULATIONS (Python Concept: Calculations & Labels)
    # -----------------------------------------------------------------------
    def update_bill_calculations(self):
        # 1. Calculate Items Subtotal
        subtotal = sum(entry["unit_price"] * entry["qty"] for entry in self.cart.values())

        # 2. Calculate Add-ons (Checkboxes)
        addons_total = 0.0
        for key, name, price in ADDONS_LIST:
            if self.addon_vars[key].get():
                addons_total += price

        # 3. Calculate Dining Packaging (Radiobutton: Dine-in vs Takeaway)
        packaging_fee = 0.50 if self.dining_option.get() == "Takeaway" else 0.0

        extra_charges = addons_total + packaging_fee

        # 4. Tax Calculation (8% on items + extras)
        taxable_amount = max(0.0, (subtotal + extra_charges) - self.applied_discount)
        tax = taxable_amount * 0.08

        # 5. Grand Total Calculation
        grand_total = max(0.0, (subtotal + extra_charges - self.applied_discount) + tax)

        # Update Live Labels
        self.lbl_subtotal.configure(text=f"${subtotal:.2f}")
        self.lbl_addons.configure(text=f"${extra_charges:.2f}")
        self.lbl_tax.configure(text=f"${tax:.2f}")
        self.lbl_discount.configure(text=f"-${self.applied_discount:.2f}")
        self.lbl_total.configure(text=f"${grand_total:.2f}")

        # Store latest values for receipt printing
        self.last_calculations = {
            "subtotal": subtotal,
            "addons_total": addons_total,
            "packaging_fee": packaging_fee,
            "extra_charges": extra_charges,
            "discount": self.applied_discount,
            "tax": tax,
            "grand_total": grand_total
        }

    # -----------------------------------------------------------------------
    # CUTE ORDER CONFIRMATION MODAL (User requested feature!)
    # -----------------------------------------------------------------------
    def confirm_and_place_order(self):
        if not self.cart:
            messagebox.showwarning("Empty Tray", "Your tray is empty! Add some sweet treats first 🧁")
            return

        self.update_bill_calculations()
        calcs = self.last_calculations

        order_id = f"#CD-{random.randint(1000, 9999)}"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        cust = self.customer_name.get().strip() or "Dreamer"
        dining = self.dining_option.get()
        tbl = self.table_number.get().strip() if dining == "Dine-in" else "Takeaway Bag"

        # Build Cute Confirmation Popup Window
        modal = tk.Toplevel(self.root)
        modal.title(f"Order Confirmed! 🌸 {order_id}")
        modal.geometry("490x700")
        modal.minsize(450, 620)
        modal.configure(bg="#FFFDFB")
        modal.transient(self.root)
        modal.grab_set()

        # Modal Canvas for receipt styling
        receipt_canvas = tk.Canvas(modal, bg="#FFFDFB", highlightthickness=0)
        receipt_scrollbar = ttk.Scrollbar(modal, orient=tk.VERTICAL, command=receipt_canvas.yview)
        receipt_content = tk.Frame(receipt_canvas, bg="#FFFDFB", padx=24, pady=16)

        receipt_content.bind(
            "<Configure>",
            lambda e: receipt_canvas.configure(scrollregion=receipt_canvas.bbox("all"))
        )
        canvas_win = receipt_canvas.create_window((0, 0), window=receipt_content, anchor="nw")
        receipt_canvas.configure(yscrollcommand=receipt_scrollbar.set)

        receipt_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        receipt_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        receipt_canvas.bind(
            "<Configure>",
            lambda e: receipt_canvas.itemconfig(canvas_win, width=e.width)
        )

        # Header Graphic Banner
        tk.Label(
            receipt_content,
            text="✦ . ⁺ . ✦ . ⁺ . ✦ . ⁺ . ✦",
            font=(self.font_family, 10),
            fg=THEME["accent_caramel"],
            bg="#FFFDFB"
        ).pack()

        tk.Label(
            receipt_content,
            text="🌸 Café de Dreams 🌸",
            font=(self.font_family, 16, "bold"),
            fg=THEME["text_dark"],
            bg="#FFFDFB"
        ).pack(pady=(4, 2))

        tk.Label(
            receipt_content,
            text="~ Where sweet dreams come true ~",
            font=(self.font_family, 9, "italic"),
            fg=THEME["text_muted"],
            bg="#FFFDFB"
        ).pack(pady=(0, 8))

        # Order & Customer Info Box
        info_box = tk.Frame(
            receipt_content,
            bg=THEME["bg_subtle"],
            highlightbackground=THEME["border_light"],
            highlightthickness=1,
            padx=12,
            pady=8
        )
        info_box.pack(fill=tk.X, pady=(0, 10))

        tk.Label(
            info_box,
            text=f"Order ID: {order_id}    •    {timestamp}",
            font=(self.font_family, 8, "bold"),
            fg=THEME["text_dark"],
            bg=THEME["bg_subtle"]
        ).pack(anchor="w")

        tk.Label(
            info_box,
            text=f"Guest: {cust}    •    Dining: {dining} ({tbl})",
            font=(self.font_family, 8),
            fg=THEME["text_muted"],
            bg=THEME["bg_subtle"]
        ).pack(anchor="w", pady=(2, 0))

        # Receipt Items Table Header
        tk.Label(
            receipt_content,
            text="─" * 46,
            font=("Consolas", 8),
            fg=THEME["border_light"],
            bg="#FFFDFB"
        ).pack()

        table_head = tk.Frame(receipt_content, bg="#FFFDFB")
        table_head.pack(fill=tk.X, pady=(2, 4))
        tk.Label(table_head, text="Item / Details", font=(self.font_family, 8, "bold"), fg=THEME["text_muted"], bg="#FFFDFB").pack(side=tk.LEFT)
        tk.Label(table_head, text="Total", font=(self.font_family, 8, "bold"), fg=THEME["text_muted"], bg="#FFFDFB").pack(side=tk.RIGHT)

        # Receipt Items List
        receipt_text_lines = []
        for key, entry in self.cart.items():
            item = entry["item"]
            size = entry["size"]
            qty = entry["qty"]
            line_cost = entry["unit_price"] * qty

            item_row = tk.Frame(receipt_content, bg="#FFFDFB")
            item_row.pack(fill=tk.X, pady=2)

            left_txt = f"{qty}x {item['name']} ({size})"
            tk.Label(item_row, text=left_txt, font=(self.font_family, 8), fg=THEME["text_dark"], bg="#FFFDFB").pack(side=tk.LEFT)
            tk.Label(item_row, text=f"${line_cost:.2f}", font=(self.font_family, 8, "bold"), fg=THEME["text_dark"], bg="#FFFDFB").pack(side=tk.RIGHT)

            receipt_text_lines.append(f"{left_txt:<32} ${line_cost:>6.2f}")

        # Active Add-ons in receipt
        active_addons = []
        for a_key, a_name, a_price in ADDONS_LIST:
            if self.addon_vars[a_key].get():
                active_addons.append((a_name, a_price))

        if active_addons:
            tk.Label(
                receipt_content,
                text="Cute Extras & Add-ons:",
                font=(self.font_family, 8, "bold"),
                fg=THEME["text_muted"],
                bg="#FFFDFB"
            ).pack(anchor="w", pady=(6, 2))

            for a_name, a_price in active_addons:
                addon_row = tk.Frame(receipt_content, bg="#FFFDFB")
                addon_row.pack(fill=tk.X, pady=1)
                tk.Label(addon_row, text=f" + {a_name}", font=(self.font_family, 7), fg=THEME["text_muted"], bg="#FFFDFB").pack(side=tk.LEFT)
                tk.Label(addon_row, text=f"${a_price:.2f}", font=(self.font_family, 7), fg=THEME["text_muted"], bg="#FFFDFB").pack(side=tk.RIGHT)
                receipt_text_lines.append(f" + {a_name:<29} ${a_price:>6.2f}")

        # Divider
        tk.Label(
            receipt_content,
            text="─" * 46,
            font=("Consolas", 8),
            fg=THEME["border_light"],
            bg="#FFFDFB"
        ).pack(pady=(4, 4))

        # Receipt Summary
        def add_receipt_summary_row(label, val_str, bold=False, color=THEME["text_dark"]):
            f = tk.Frame(receipt_content, bg="#FFFDFB")
            f.pack(fill=tk.X, pady=1)
            f_font = (self.font_family, 9, "bold" if bold else "normal")
            tk.Label(f, text=label, font=f_font, fg=color, bg="#FFFDFB").pack(side=tk.LEFT)
            tk.Label(f, text=val_str, font=f_font, fg=color, bg="#FFFDFB").pack(side=tk.RIGHT)

        add_receipt_summary_row("Subtotal:", f"${calcs['subtotal']:.2f}")
        if calcs['extra_charges'] > 0:
            add_receipt_summary_row("Add-ons & Packaging:", f"${calcs['extra_charges']:.2f}")
        if calcs['discount'] > 0:
            add_receipt_summary_row("Discount Saved:", f"-${calcs['discount']:.2f}", color=THEME["price_green"])
        add_receipt_summary_row("Tax (8%):", f"${calcs['tax']:.2f}")
        add_receipt_summary_row("Total Paid:", f"${calcs['grand_total']:.2f}", bold=True, color=THEME["accent_caramel"])

        # Cute Mascot ASCII & Note
        mascot_frame = tk.Frame(receipt_content, bg="#FBF6EE", padx=10, pady=8)
        mascot_frame.pack(fill=tk.X, pady=(12, 8))

        mascot_art = """
   (\\__/)
   (='.'=)  ♥ "Baked with fairy dust & love!"
   (")_(")     Estimated wait: 8 - 12 mins
"""
        tk.Label(
            mascot_frame,
            text=mascot_art,
            font=("Consolas", 8),
            fg=THEME["text_dark"],
            bg="#FBF6EE",
            justify="left"
        ).pack()

        # Receipt Action Buttons: Save to text file & Close
        btn_box = tk.Frame(receipt_content, bg="#FFFDFB")
        btn_box.pack(fill=tk.X, pady=(8, 4))

        def save_receipt_file():
            filename = f"Receipt_{order_id.replace('#', '')}.txt"
            content = f"""==================================================
           🌸 CAFÉ DE DREAMS 🌸
         ~ Virtual Café Receipt ~
==================================================
Order ID:   {order_id}
Date/Time:  {timestamp}
Customer:   {cust}
Dining:     {dining} ({tbl})
--------------------------------------------------
ITEMS:
""" + "\n".join(receipt_text_lines) + f"""
--------------------------------------------------
Subtotal:                ${calcs['subtotal']:.2f}
Addons & Packaging:      ${calcs['extra_charges']:.2f}
Discount:               -${calcs['discount']:.2f}
Tax (8%):                ${calcs['tax']:.2f}
==================================================
TOTAL PAID:              ${calcs['grand_total']:.2f}
==================================================

  (\\__/)
  (='.'=)  ♥ "Thank you for visiting Café de Dreams!"
  (")_(")     Please come again soon!
=================================================="""

            try:
                save_path = filedialog.asksaveasfilename(
                    initialfile=filename,
                    defaultextension=".txt",
                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
                )
                if save_path:
                    with open(save_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    messagebox.showinfo("Receipt Saved", f"Receipt successfully saved to:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save receipt: {e}")

        save_btn = tk.Button(
            btn_box,
            text="💾 Save Receipt to File",
            font=(self.font_family, 8, "bold"),
            bg="#EAE0D3",
            fg=THEME["text_dark"],
            relief=tk.FLAT,
            padx=10,
            pady=4,
            cursor="hand2",
            command=save_receipt_file
        )
        save_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 4))

        def close_and_reset():
            modal.destroy()
            self.cart.clear()
            self.applied_discount = 0.0
            self.update_cart_display()
            self.status_message.set(f"Order {order_id} placed successfully! Thank you {cust} 🌸")

        done_btn = tk.Button(
            btn_box,
            text="✨ Done / New Order",
            font=(self.font_family, 8, "bold"),
            bg=THEME["accent_caramel"],
            fg="#FFFFFF",
            relief=tk.FLAT,
            padx=10,
            pady=4,
            cursor="hand2",
            command=close_and_reset
        )
        done_btn.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(4, 0))


# ---------------------------------------------------------------------------
# APPLICATION ENTRY POINT
# ---------------------------------------------------------------------------
def main():
    root = tk.Tk()

    # Enable High-DPI scaling on Windows for ultra sharp rendering
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

    app = CafeDeDreamsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
