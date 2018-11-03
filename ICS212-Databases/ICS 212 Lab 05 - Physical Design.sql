--
--   ICS 212 Lab 05 - create schema
-- 
-- ===========================================================================
-- Create customers table.
-- ===========================================================================

CREATE TABLE customers
    ( customer_id        NUMBER(6)     
    , cust_first_name    VARCHAR2(20) 
    CONSTRAINT cust_fname_nn NOT NULL
    , cust_last_name     VARCHAR2(20) 
    CONSTRAINT cust_lname_nn NOT NULL
    , nls_language       VARCHAR2(3)
    , nls_territory      VARCHAR2(30)
    , credit_limit       NUMBER(9,2)
    , cust_email         VARCHAR2(30)
    , account_mgr_id     NUMBER(6)
    , CONSTRAINT customers_pk PRIMARY KEY (customer_id)
    )

-- ===========================================================================
-- Create warehouses table
-- ===========================================================================

CREATE TABLE warehouses
    ( warehouse_id       NUMBER(3) 
    , warehouse_name     VARCHAR2(35)
    , location_id        NUMBER(4)
    , CONSTRAINT warehouses_pk PRIMARY KEY (warehouse_id)
    ) ;

-- ===========================================================================
-- Create table order_items, which contains a concatenated primary key
-- ===========================================================================
	
CREATE TABLE order_items
    ( order_id           NUMBER(12) 
    , line_item_id       NUMBER(3)  NOT NULL
    , product_id         NUMBER(6)  NOT NULL
    , unit_price         NUMBER(8,2)
    , quantity           NUMBER(8)
    , CONSTRAINT order_items_pk PRIMARY KEY (order_id, line_item_id)
    ) ;

-- ===========================================================================
-- Create table orders
-- ===========================================================================

CREATE TABLE orders
    ( order_id           NUMBER(12)
    , order_date         DATE
    CONSTRAINT order_date_nn NOT NULL
    , order_mode         VARCHAR2(8)
    , customer_id        NUMBER(6) 
    CONSTRAINT order_customer_id_nn NOT NULL
    , order_status       NUMBER(2)
    , order_total        NUMBER(8,2)
    , sales_rep_id       NUMBER(6)
    , promotion_id       NUMBER(6)
    , CONSTRAINT order_pk PRIMARY KEY (order_id)
    )
    -- Partition Orders on Order Dates as a range of 1 day per partition.
PARTITION BY RANGE (order_date)
INTERVAL(NUMTOYMINTERVAL(1, 'DAY'))
(PARTITION olddata VALUES LESS THAN (TO_DATE('01-JAN-2008','DD-MON-YYYY'))
);

-- ===========================================================================
-- Create inventories table, which contains a concatenated primary key.
-- ===========================================================================
    
CREATE TABLE inventories
  ( product_id         NUMBER(6)
  , warehouse_id       NUMBER(3) 
  CONSTRAINT inventory_warehouse_id_nn NOT NULL
  , quantity_on_hand   NUMBER(8)
  CONSTRAINT inventory_qoh_nn NOT NULL
  , CONSTRAINT inventory_pk PRIMARY KEY (product_id, warehouse_id)
  ) ;

-- ===========================================================================
-- Create table product_information
-- ===========================================================================

-- Create cluster

CREATE CLUSTER product_information_cluster
  (product_id NUMBER(6))
  SIZE 512;

  CREATE INDEX idx_product_info_cluster ON CLUSTER product_information_cluster

CREATE TABLE product_information
    ( product_id          NUMBER(6)
    , product_name        VARCHAR2(50)
    , product_description VARCHAR2(2000)
    , category_id         NUMBER(2)
    , weight_class        NUMBER(1)
    , warranty_period     NUMBER(5)
    , supplier_id         NUMBER(6)
    , product_status      VARCHAR2(20)
    , list_price          NUMBER(8,2)
    , min_price           NUMBER(8,2)
    , catalog_url         VARCHAR2(50)
    , CONSTRAINT product_information_pk PRIMARY KEY (product_id)
    )

    CLUSTER product_information_cluster(product_id)

-- Partition product_info on each category
PARTITION BY REFERENCE (category_id);

-- ===========================================================================
-- Create table product_descriptions, which contains NVARCHAR2 columns for
-- NLS-language information.
-- ===========================================================================

CREATE TABLE product_descriptions
    ( product_id             NUMBER(6)
    , language_id            VARCHAR2(3)
    , translated_name        NVARCHAR2(50)
    CONSTRAINT translated_name_nn NOT NULL
    , translated_description NVARCHAR2(2000)
    CONSTRAINT translated_desc_nn NOT NULL
    , CONSTRAINT product_descriptions_pk 
    PRIMARY KEY (product_id, language_id)
    );


-- ===========================================================================
-- Create foreign key constraints now that all tables are in place.
-- ===========================================================================

ALTER TABLE orders 
ADD ( CONSTRAINT orders_customer_id_fk 
      FOREIGN KEY (customer_id) 
      REFERENCES customers(customer_id) 
      ON DELETE SET NULL 
    ) ;

ALTER TABLE inventories 
ADD ( CONSTRAINT inventories_warehouses_fk 
      FOREIGN KEY (warehouse_id)
      REFERENCES warehouses (warehouse_id)
    ) ;

ALTER TABLE inventories 
ADD ( CONSTRAINT inventories_product_id_fk 
      FOREIGN KEY (product_id)
      REFERENCES product_information (product_id)
    ) ;

ALTER TABLE order_items
ADD ( CONSTRAINT order_items_order_id_fk 
      FOREIGN KEY (order_id)
      REFERENCES orders(order_id)
      ON DELETE CASCADE
    ) ;

ALTER TABLE order_items
ADD ( CONSTRAINT order_items_product_id_fk 
      FOREIGN KEY (product_id)
      REFERENCES product_information(product_id)
    ) ;

ALTER TABLE product_descriptions
ADD ( CONSTRAINT pd_product_id_fk
      FOREIGN KEY (product_id)
      REFERENCES product_information(product_id)
    ) ;


-- Create Indexes for Customer Table

CREATE INDEX customer_i01
ON customer(account_mgr_id);
CREATE INDEX orders_i02
ON customer(nls_language);
CREATE INDEX orders_i03
ON customer(nls_territory);

-- Create Indexes for Orders Table

CREATE INDEX orders_i01
ON orders(customer_id);
CREATE INDEX orders_i02
ON orders(order_date);
CREATE INDEX orders_i03
ON orders(order_status);
CREATE INDEX orders_i04
ON orders(sales_rep_id);
CREATE INDEX orders_i05
ON orders(promotion_id);

-- Create Indexes for Order Items Table

CREATE INDEX order_items_i01
ON order_items(product_id);

-- Create Indexes for Inventories Table

CREATE INDEX inventories_i01
ON inventories(quantity_on_hand);

-- Create Indexes for Warehouses Table

CREATE INDEX warehouses_i01
ON warehouses(location_id);
CREATE INDEX warehouses_i02
ON warehouses(warehouse_name);

commit;