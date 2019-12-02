''' Simple TKinter used Restaurant System'''
from tkinter import *
from rms import *
from NewMain import *

class main(object):
    def __init__(self):
        self.restaurant = []
        self.customer = []
        self.list_restaurant = []
        self.waiter = ['Sohel','Amin']


    def add_customer(self, name, address, phone_no, check_in):
        self.cus = Customer(name, address, phone_no)
        for r in self.restaurant:
            if r.name == check_in:
                r.customer.append(self.cus)
                self.cus.restaurant = r
        self.customer.append(self.cus)


    def add_menu(self, item_name, price, item_type, restaurant):
        self.menu = None
        if item_type == "Drinks":
            self.menu = Drinks(item_name, price)
        elif item_type == "Snacks":
            self.menu = Snacks(item_name, price)
        elif item_type == "Main_Food":
            self.menu = Main_Food(item_name, price)

        for res in self.restaurant:
            if res.name == restaurant:
                res.addMenu(self.menu)
    
    def print_restaurant(self):
        for r in self.restaurant:
            print(r.name, r.location, r.city)
        
    def print_menu(self):
        for r in self.restaurant:
            for m in r.menu:
                print('Restaurant ', r.name, 'have :', m.name, 'price:', m.price)
            print(r.name, r.location, r.city)

main_obj = main()

class Main_Window(Frame):
    def __init__(self, master):
        super(Main_Window, self).__init__(master)
        self.grid()
        self.configure(padx = 20, pady = 20)
        self.createMenu()
        self.createCustomer()
        #self.create_menu()
        self.add_menu(master)
        
    def createMenu(self):    
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        varBurgers=StringVar()
        varPizza=StringVar()
        varBiriyani=StringVar()
        def chkFries():
            if (var1.get()==1):
                txtBurger.configure(state=NORMAL)
                varBurgers.set("")
            elif(var1.get()==0):
                txtBurger.configure(state=DISABLED)
                varBurgers.set("0")


        def chkMomo():
            if (var2.get()==1):
                txtPizza.configure(state=NORMAL)
                varPizza.set("")
            elif(var2.get()==0):
                txtPizza.configure(state=DISABLED)
                varPizza.set("0")
        def chkWings():
            if (var3.get()==1):
                txtBiriyani.configure(state=NORMAL)
                varBiriyani.set("")
            elif(var3.get()==0):
                txtBiriyani.configure(state=DISABLED)
                varBiriyani.set("0")
        Burger= Checkbutton (self, text="Fries  \t\t 220 BDT",variable=var1,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkFries).grid(row=1,column=0,sticky='w')
        txtBurger=Entry(self,font=('arial',13,'bold'), textvariable=varBurgers ,width=6,justify='right',state=DISABLED)
        txtBurger.grid(row=1,column =1)

        Pizza= Checkbutton (self, text="Chicken Pizza\t 450 BDT",variable=var2,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkMomo).grid(row=2,column=0,sticky='w')
        txtPizza= Entry(self,font=('arial',13,'bold'), textvariable=varPizza ,width=6,justify='right',state=DISABLED)
        txtPizza.grid(row=2,column =1)

        Biriyani= Checkbutton (self, text="Chicken Biriyani\t 220 BDT",variable=var3,onvalue=1, offvalue=0,font=('arial',13,'bold'),command=chkWings).grid(row=3,column=0,sticky='w')
        txtBiriyani= Entry(self,font=('arial',13,'bold'), textvariable=varBiriyani,width=6,justify='right',state=DISABLED)
        txtBiriyani.grid(row=3,column =1)
        self.total=0
        self.total=(220*var1.get())+(450*var2.get())+(220*var3.get())
        print(self.total)
        lblMeal=Label(self, font=('arial', 18,'bold'), text="Total: "+str(self.total))
        lblMeal.grid(row=6,column=0)
        
        btnCalculate=Button(self, font=('arial', 18,'bold'), text="Calculate", command = self.calculate)
        btnCalculate.grid(row=4,column=0)

    
    def createCustomer(self):
        self.cus_labelframe = LabelFrame(self, text="Customer", padx = 20, pady = 20)
        self.cus_labelframe.grid(padx = 10, pady = 0)
 
        self.cus_lbl_name = Label(self.cus_labelframe, text="Name:",  padx = 10, pady = 10)
        self.cus_lbl_name.grid(row = 0, column = 0)
        self.cus_ent_name = Entry(self.cus_labelframe, width = 50)
        self.cus_ent_name.grid(row = 0, column = 1)
        self.cus_bttn_add = Button(self.cus_labelframe, text = '   Add Customer   ', command = self.add_customer)
        self.cus_bttn_add.grid(row = 0, column = 2, padx = 10, pady = 10)

        self.cus_lbl_Address = Label(self.cus_labelframe, text="Address:",  padx = 10, pady = 10)
        self.cus_lbl_Address.grid(row = 1, column = 0)
        self.cus_ent_Address = Entry(self.cus_labelframe, width = 50)
        self.cus_ent_Address.grid(row = 1, column = 1)

        self.cus_lbl_phone_no = Label(self.cus_labelframe, text="Phone No:" , padx = 10, pady = 10)
        self.cus_lbl_phone_no.grid(row = 2, column = 0)
        self.cus_ent_phone_no = Entry(self.cus_labelframe, width = 50)
        self.cus_ent_phone_no.grid(row = 2, column = 1)

        self.cus_lbl_waiter = Label(self.cus_labelframe, text="Waiter" , padx = 10, pady = 10)
        self.cus_lbl_waiter.grid(row = 3, column = 0)
        from tkinter.ttk import Combobox
        self.cus_combo_waiters = Combobox(self.cus_labelframe, values = main_obj.waiter, width = 50)
        self.cus_combo_waiters.grid(row = 3, column = 1, padx = 10, pady = 10)
        
   

    def calculate(self):
        print(self.total)
    
    def add_customer(self):
        name = self.cus_ent_name.get()
        address = self.cus_ent_Address.get()
        phone_no = self.cus_ent_phone_no.get()
        waiter = self.cus_combo_waiters.get()
        #main_obj.add_customer(name, address, phone_no, waiter)
        #self.cus_ent_name.delete(0, 'end')
        #self.cus_ent_Address.delete(0, 'end')
        #self.cus_ent_phone_no.delete(0, 'end')
        #self.cus_ent_name.focus_set()
        print('Customer: ', name, address, phone_no,waiter, "Added.")

    def create_menu(self):
        self.menu_labelframe = LabelFrame(self, text="Food Menu", padx = 20, pady = 20)
        self.menu_labelframe.grid(padx = 10, pady = 0)
 
        self.menu_lbl_name = Label(self.menu_labelframe, text="Name:",  padx = 10, pady = 10)
        self.menu_lbl_name.grid(row = 0, column = 0)
        self.menu_ent_name = Entry(self.menu_labelframe, width = 50)
        self.menu_ent_name.grid(row = 0, column = 1)
        self.menu_bttn_add = Button(self.menu_labelframe, text = '   Add Food Menu   ', command = self.add_created_menu)
        self.menu_bttn_add.grid(row = 0, column = 2, padx = 10, pady = 10)

        self.menu_lbl_price = Label(self.menu_labelframe, text="Price:",  padx = 10, pady = 10)
        self.menu_lbl_price.grid(row = 1, column = 0)
        self.menu_ent_price = Entry(self.menu_labelframe, width = 50)
        self.menu_ent_price.grid(row = 1, column = 1)

        self.menu_lbl_menutype = Label(self.menu_labelframe, text="Menu Type" , padx = 10, pady = 10)
        self.menu_lbl_menutype.grid(row = 3, column = 0)
        list_menu = ['Snacks', 'Drinks', 'Main_Food']
        from tkinter.ttk import Combobox
        self.menu_combo_menu_type = Combobox(self.menu_labelframe, values = list_menu, width = 50)
        self.menu_combo_menu_type.grid(row = 3, column = 1, padx = 10, pady = 10)

        self.menu_lbl_restaurant = Label(self.menu_labelframe, text="Restaurant" , padx = 10, pady = 10)
        self.menu_lbl_restaurant.grid(row = 4, column = 0)
        from tkinter.ttk import Combobox
        self.menu_combo_restaurant = Combobox(self.menu_labelframe, values = main_obj.list_restaurant, width = 50)
        self.menu_combo_restaurant.grid(row = 4, column = 1, padx = 10, pady = 10)
    
    def add_restaurant(self):
        name = self.res_ent_name.get()
        location = self.res_ent_location.get()
        city = self.res_ent_city.get()
        main_obj.add_restaurant(name, location, city)
        self.res_ent_name.delete(0, 'end')
        self.res_ent_location.delete(0, 'end')
        self.res_ent_city.delete(0, 'end')
        self.res_ent_name.focus_set()
        main_obj.list_restaurant.append(name)
        print('Restaurant: ', name, location, city, "Added.")
        self.refresh_customer()

    def refresh_customer(self):
        self.cus_labelframe.grid_forget()
        self.create_customer_widgets()
        self.menu_labelframe.grid_forget()
        self.create_menu()

    def add_customer(self):
        name = self.cus_ent_name.get()
        address = self.cus_ent_Address.get()
        phone_no = self.cus_ent_phone_no.get()
        check_in = self.cus_combo_restaurant.get()
        main_obj.add_customer(name, address, phone_no, check_in)
        self.cus_ent_name.delete(0, 'end')
        self.cus_ent_Address.delete(0, 'end')
        self.cus_ent_phone_no.delete(0, 'end')
        self.cus_ent_name.focus_set()
        print('Customer: ', name, address, phone_no, "Added.")

    def add_created_menu(self):
        item_name = self.menu_ent_name.get()
        item_price = int(self.menu_ent_price.get())
        item_type = self.menu_combo_menu_type.get()
        restaurant = self.menu_combo_restaurant.get()
        main_obj.add_menu(item_name, item_price, item_type, restaurant)
        self.menu_ent_name.delete(0, 'end')
        self.menu_ent_price.delete(0, 'end')
        self.menu_combo_menu_type.delete(0, 'end')
        self.menu_combo_restaurant.delete(0, 'end')
        main_obj.print_menu()
        



    def add_menu(self, master):
        # Creating a Menu Bar
        """
        master.menuBar = Menu(root)
        master.config(menu=master.menuBar)
        p_res_add = popup_add_restaurant()
        p_cus_add = popup_add_customer()
        # Add File menu items
        fileMenu = Menu(master.menuBar, tearoff=0)
        newMenu = Menu(master.menuBar, tearoff=0)
        newMenu.add_command(label = "Customer", command = p_cus_add.call_popup)
        newMenu.add_command(label = "Restaurant", command = p_res_add.call_popup)
        fileMenu.add_cascade(label = "New", menu = newMenu)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        master.menuBar.add_cascade(label="File", menu=fileMenu)

        # Add Edit menu items
        editMenu = Menu(master.menuBar, tearoff=0)
        editMenu.add_command(label="Cut")
        editMenu.add_command(label="Copy")
        editMenu.add_command(label="Paste")
        master.menuBar.add_cascade(label="Edit", menu=editMenu)


        # Add Customer menu items
        cusMenu = Menu(master.menuBar, tearoff=0)
        cus_table = customer_table()
        cusMenu.add_command(label="Show", command = cus_table.create_table)
        cusMenu.add_command(label="Add new", command = p_cus_add.call_popup)
        cusMenu.add_command(label="Delete")
        cusMenu.add_command(label="Status")
        order = popup_order()
        cusMenu.add_command(label="Order", command = order.call_popup_customer)
        master.menuBar.add_cascade(label="Customer", menu=cusMenu)

        # Add Restaurant menu items
        resMenu = Menu(master.menuBar, tearoff=0)
        res_table = restaurant_table()
        resMenu.add_command(label="Show", command = res_table.create_table)
        resMenu.add_command(label="Add new", command = p_res_add.call_popup)
        resMenu.add_command(label="Delete")
        resMenu.add_command(label="Status")
        resMenu.add_command(label="Orders")
        resMenu.add_command(label="Payments")
        master.menuBar.add_cascade(label="Restaurant", menu=resMenu)

        # Add Help menu and about item
        helpMenu = Menu(master.menuBar, tearoff=0)
        helpMenu.add_command(label="About")
        master.menuBar.add_cascade(label="Help", menu=helpMenu)
        """

        # Exit GUI Cleanly
    def _quit(self):
        self.quit()
        self.destroy()
        exit()
        
        
        
        
        
        
        
        
        
        
        
        
        

class popup_add_restaurant(object):
    def __init__(self):
        pass
    def call_popup(self):
        top = Toplevel()
        self.res_labelframe = LabelFrame(top, text="Restaurant", padx = 20, pady = 20)
        self.res_labelframe.grid()
 
        self.res_lbl_name = Label(self.res_labelframe, text="Name:", padx = 10, pady = 10)
        self.res_lbl_name.grid(row = 0, column = 0)
        self.res_ent_name = Entry(self.res_labelframe, width = 50)
        self.res_ent_name.grid(row = 0, column = 1)
        self.res_bttn_add = Button(self.res_labelframe, text = 'Add Restaurant', command = self.add_restaurant)
        self.res_bttn_add.grid(row = 0, column = 2, padx = 10, pady = 10)

        self.res_lbl_location = Label(self.res_labelframe, text="Location:",  padx = 10, pady = 10)
        self.res_lbl_location.grid(row = 1, column = 0)
        self.res_ent_location = Entry(self.res_labelframe, width = 50)
        self.res_ent_location.grid(row = 1, column = 1)

        self.res_lbl_city = Label(self.res_labelframe, text="City:" , padx = 10, pady = 10)
        self.res_lbl_city.grid(row = 2, column = 0)
        self.res_ent_city = Entry(self.res_labelframe, width = 50)
        self.res_ent_city.grid(row = 2, column = 1)

        self.res_ent_name.focus_set()

        self.add_waiters = BooleanVar()
        Checkbutton(self.res_labelframe, text = "Add Waiters", onvalue = 0 ,variable = self.add_waiters).grid(row = 3, column = 0, sticky = W, padx = 10, pady = 10)
        self.add_tables = BooleanVar()
        Checkbutton(self.res_labelframe, text = "Add Tables", onvalue = 0 ,variable = self.add_tables).grid(row = 3, column = 1, sticky = W, padx = 100, pady = 10)
        self.add_menus = BooleanVar()
        Checkbutton(self.res_labelframe, text = "Add Menus", variable = self.add_menus).grid(row = 3, column = 2, sticky = W, padx = 10, pady = 10)

    def add_restaurant(self):
        name = self.res_ent_name.get()
        location = self.res_ent_location.get()
        city = self.res_ent_city.get()
        main_obj.add_restaurant(name, location, city)
        self.res_ent_name.delete(0, 'end')
        self.res_ent_location.delete(0, 'end')
        self.res_ent_city.delete(0, 'end')
        self.res_ent_name.focus_set()
        main_obj.list_restaurant.append(name)
        print('Restaurant: ', name, location, city, "Added.")

class popup_order(object):
    def __init__(self):
        pass

    def call_popup_customer(self):
        self.top = Toplevel()
        self.order_labelframe = LabelFrame(self.top, text="Select Customer", padx = 20, pady = 20)
        self.order_labelframe.grid(padx = 10, pady = 0)
 
        self.order_lbl_name = Label(self.order_labelframe, text="Customer:",  padx = 10, pady = 10)
        self.order_lbl_name.grid(row = 0, column = 0)
        self.list_cus = []
        for c in main_obj.customer:
            self.list_cus.append(c.name)
        from tkinter.ttk import Combobox
        self.order_combo_customer = Combobox(self.order_labelframe, values = self.list_cus, width = 50)
        self.order_combo_customer.grid(row = 0, column = 1, padx = 10, pady = 10)
    
        self.order_bttn_add = Button(self.order_labelframe, text = '   Select Customer   ', command = self.call_popup_order)
        self.order_bttn_add.grid(row = 0, column = 2, padx = 10, pady = 10)

    def call_popup_order(self):
        #top = Toplevel()
        self.order_labelframe.grid_forget()
        self.order_labelframe = LabelFrame(self.top, text="Order", padx = 20, pady = 20)
        self.order_labelframe.grid(padx = 10, pady = 0)
 
        self.order_lbl_item = Label(self.order_labelframe, text="Item:",  padx = 10, pady = 10)
        self.order_lbl_item.grid(row = 0, column = 0)
        self.list_menu = []
        for r in main_obj.restaurant:
            for c in r.customer:
                if c.name == self.order_combo_customer.get():
                    for m in r.menu:
                        self.list_menu.append(m.name)
        from tkinter.ttk import Combobox
        self.order_combo_menu = Combobox(self.order_labelframe, values = self.list_menu, width = 50)
        self.order_combo_menu.grid(row = 0, column = 1, padx = 10, pady = 10)
    
        self.order_bttn_add = Button(self.order_labelframe, text = '   Place Order   ', command = self.place_order)
        self.order_bttn_add.grid(row = 0, column = 2, padx = 10, pady = 10)

        self.order_lbl_qnt = Label(self.order_labelframe, text="Quantity:" , padx = 10, pady = 10)
        self.order_lbl_qnt.grid(row = 1, column = 0)
        self.order_ent_qnt = Entry(self.order_labelframe, width = 50)
        self.order_ent_qnt.grid(row = 1, column = 1)

    def place_order(self):
        customer = self.order_combo_customer.get()
        menu_name = self.order_combo_menu.get()
        self.cus = None
        self.menu  = None
        for cus in main_obj.customer:
            if cus.name == customer:
                self.cus = cus
        for res in main_obj.restaurant:
            for m in res.menu:
                if m.name == menu_name:
                    self.menu = m
        qnt = int(self.order_ent_qnt.get())
        self.cus.OrderFood(self.menu, qnt)
        print('Customer', customer, 'Ordered', menu_name, 'Quantity:', qnt)


class popup_add_customer(object):
    def __init__(self):
        pass
    def call_popup(self):
        top = Toplevel()
        self.cus_labelframe = LabelFrame(top, text="Customer", padx = 20, pady = 20)
        self.cus_labelframe.grid(padx = 10, pady = 0)
 
        self.cus_lbl_name = Label(self.cus_labelframe, text="Name:",  padx = 10, pady = 10)
        self.cus_lbl_name.grid(row = 0, column = 0)
        self.cus_ent_name = Entry(self.cus_labelframe, width = 50)
        self.cus_ent_name.grid(row = 0, column = 1)
        self.cus_bttn_add = Button(self.cus_labelframe, text = '   Add Customer   ', command = self.add_customer)
        self.cus_bttn_add.grid(row = 0, column = 2, padx = 10, pady = 10)

        self.cus_lbl_Address = Label(self.cus_labelframe, text="Address:",  padx = 10, pady = 10)
        self.cus_lbl_Address.grid(row = 1, column = 0)
        self.cus_ent_Address = Entry(self.cus_labelframe, width = 50)
        self.cus_ent_Address.grid(row = 1, column = 1)

        self.cus_lbl_phone_no = Label(self.cus_labelframe, text="Phone No:" , padx = 10, pady = 10)
        self.cus_lbl_phone_no.grid(row = 2, column = 0)
        self.cus_ent_phone_no = Entry(self.cus_labelframe, width = 50)
        self.cus_ent_phone_no.grid(row = 2, column = 1)

        self.cus_lbl_checkIn = Label(self.cus_labelframe, text="Check In To:" , padx = 10, pady = 10)
        self.cus_lbl_checkIn.grid(row = 3, column = 0)
        from tkinter.ttk import Combobox
        self.cus_combo_restaurant = Combobox(self.cus_labelframe, values = main_obj.list_restaurant, width = 50)
        self.cus_combo_restaurant.grid(row = 3, column = 1, padx = 10, pady = 10)

    def add_customer(self):
        name = self.cus_ent_name.get()
        address = self.cus_ent_Address.get()
        phone_no = self.cus_ent_phone_no.get()
        check_in = self.cus_combo_restaurant.get()
        main_obj.add_customer(name, address, phone_no, check_in)
        self.cus_ent_name.delete(0, 'end')
        self.cus_ent_Address.delete(0, 'end')
        self.cus_ent_phone_no.delete(0, 'end')
        self.cus_ent_name.focus_set()
        print('Customer: ', name, address, phone_no, "Added.")

class customer_table(Frame):
    def __init__(self):
        pass

    def create_table(self):
        parent = Toplevel()
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = W)
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        self.frame1= Frame(self)
        self.frame2= Frame(self)
        from tkinter.ttk import Treeview
        tv = Treeview(self)
        tv['columns'] = ('address', 'phone_no', 'check_in', 'waiter', 'table', 'bill')
        tv.heading("#0", text='Customer Name', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('address', text='Address')
        tv.column('address', anchor='center', width=100)
        tv.heading('phone_no', text='Phone No.')
        tv.column('phone_no', anchor='center', width=100)
        tv.heading('check_in', text='Check In To')
        tv.column('check_in', anchor='center', width=100)
        tv.heading('waiter', text='Waiter')
        tv.column('waiter', anchor='center', width=100)
        tv.heading('table', text='Table No.')
        tv.column('table', anchor='center', width=100)
        tv.heading('bill', text='Current Bill')
        tv.column('bill', anchor='center', width=100)
        tv.grid(sticky = (N, S, W, E))
        self.frame1.treeview = tv
        self.frame1.grid_rowconfigure(0, weight = 1)
        self.frame1.grid_columnconfigure(0, weight = 1)
        self.frame2.grid(row = 0, column = 1, sticky = N)
        self.button = Button(self.frame2, text= "Add")
        self.button.grid(row = 0, column = 0)
        self.button1 = Button(self.frame2, text= "Modify")
        self.button1.grid(row = 1, column = 0)
        self.button2 = Button(self.frame2, text= "Delete")
        self.button2.grid(row = 2, column = 0)
        self.button3 = Button(self.frame2, text= "Delete All")
        self.button3.grid(row = 3, column = 0)

    def LoadTable(self):
        for cus in main_obj.customer:
            name = cus.name
            address = cus.address
            phone_no = cus.phone_no
            res = cus.restaurant.name
            #waiter = cus.waiter.name
            #table = cus.table.id
            bill = cus.total_cost
            self.frame1.treeview.insert('', 'end', text=name, values=(address, phone_no, res, "", "", bill))


class restaurant_table(Frame):
    def __init__(self):
        pass

    def create_table(self):
        parent = Toplevel()
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = W)
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        self.frame1= Frame(self)
        self.frame2= Frame(self)
        from tkinter.ttk import Treeview
        tv = Treeview(self)
        tv['columns'] = ('location', 'city', 'cutomer_count', 'total_table', 'total_waiter', 'sales')
        tv.heading("#0", text='Restaurant name', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('location', text='Location')
        tv.column('location', anchor='center', width=100)
        tv.heading('city', text='City')
        tv.column('city', anchor='center', width=100)
        tv.heading('cutomer_count', text='Customer Count')
        tv.column('cutomer_count', anchor='center', width=100)
        tv.heading('total_table', text='Total Table')
        tv.column('total_table', anchor='center', width=100)
        tv.heading('total_waiter', text='Total Waiter')
        tv.column('total_waiter', anchor='center', width=100)
        tv.heading('sales', text='Sales')
        tv.column('sales', anchor='center', width=100)
        tv.grid(sticky = (N, S, W, E))
        self.frame1.treeview = tv
        self.frame1.grid_rowconfigure(0, weight = 1)
        self.frame1.grid_columnconfigure(0, weight = 1)
        self.frame2.grid(row = 0, column = 1, sticky = N)
        self.button = Button(self.frame2, text= "Add")
        self.button.grid(row = 0, column = 0)
        self.button1 = Button(self.frame2, text= "Modify")
        self.button1.grid(row = 1, column = 0)
        self.button2 = Button(self.frame2, text= "Delete")
        self.button2.grid(row = 2, column = 0)
        self.button3 = Button(self.frame2, text= "Delete All")
        self.button3.grid(row = 3, column = 0)

    def LoadTable(self):
        for res in main_obj.restaurant:
            name = res.name
            location = res.location
            city = res.city
            self.frame1.treeview.insert('', 'end', text=name, values=(location, city, '??', 10, 10, '0.00'))


if __name__=="__main__":
    root = Tk()
    #modify the window
    root.title('Restaurant System') 
    root.geometry('800x800')
    app = Main_Window(root)
    # kick off the windows event loop
    root.mainloop()
   
