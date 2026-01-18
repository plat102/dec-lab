import psycopg2
from config import load_config
from psycopg2.extras import execute_values

def insert_vendor(vendor_name):
    """ Insert a new vendor into the vendors table """

    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""

    vendor_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (vendor_name,))

                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    vendor_id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return vendor_id

def insert_many_vendors(vendor_list):
    """ Insert multiple vendors into the vendors table
    - executemany: run multiple insert
    - execute_values: 1 bulk
    """

    # sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING *" # C1
    sql = "INSERT INTO vendors(vendor_name) VALUES %s RETURNING *" # C2

    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                # cur.executemany(sql, vendor_list)
                execute_values(cur, sql, vendor_list)

                rows = cur.fetchall()
                print(rows)
                vendor_ids = [row[0] for row in rows]

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return vendor_ids


def insert_many_parts(part_list):
    """ Insert multiple parts into the parts table """

    sql = "INSERT INTO parts(part_name) VALUES %s ON CONFLICT DO NOTHING RETURNING *"

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                execute_values(cur, sql, part_list)
                rows = cur.fetchall()
                print(f"Inserted {len(rows)} parts.")
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def assign_parts_to_vendors(vendor_part_list):
    """
    Link parts to vendors
    Input: List of tuples ('Part Name', 'Vendor Name')
    """

    # Find vendor & part -> insert to relationship table
    sql = """
        INSERT INTO vendor_parts (part_id, vendor_id)
        VALUES (
            (SELECT part_id FROM parts WHERE part_name = %s LIMIT 1), \
            (SELECT vendor_id FROM vendors WHERE vendor_name = %s LIMIT 1)    
        ) ON CONFLICT DO NOTHING; \
    """

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # use executemany for subquery
                cur.executemany(sql, vendor_part_list)

                print(f"Linked {cur.rowcount} relationships.")
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    inserted_id = insert_vendor("3M Cexo.")
    print(inserted_id)

    inserted_ids = insert_many_vendors([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])
    print(inserted_ids)

    parts = [
        ('Antenna',),
        ('Home Button',),
        ('LTE Modem',),
        ('SIM Tray',),
        ('Speaker',),
        ('Vibrator',)
    ]
    print("\n--- Inserting Parts ---")
    insert_many_parts(parts)

    # 3. match part & vendor
    part_vendor_relations = [
        ('Antenna', 'Foster Electric Co. Ltd.'),
        ('Antenna', 'Murata Manufacturing Co. Ltd.'),
        ('Home Button', 'Dynacast International Inc.'),
        ('Home Button', '3M Corp'),
        ('LTE Modem', 'Dynacast International Inc.'),
        ('LTE Modem', '3M Corp'),
        ('SIM Tray', 'AKM Semiconductor Inc.'),
        ('SIM Tray', '3M Corp'),
        ('Speaker', 'Daikin Industries Ltd.'),
        ('Speaker', 'Asahi Glass Co Ltd.'),
        ('Vibrator', 'Dynacast International Inc.'),
        ('Vibrator', 'Foster Electric Co. Ltd.')
    ]
    print("\n--- Linking Vendors & Parts ---")
    assign_parts_to_vendors(part_vendor_relations)
