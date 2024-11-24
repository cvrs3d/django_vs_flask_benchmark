def generate_order_urls(base_url, num_records, output_file):
    with open(output_file, 'w') as file:
        for i in range(1, num_records + 1):
            url = f"{base_url}/api/orders/{i}/\n"
            file.write(url)


if __name__ == "__main__":
    BASE_URL = ""
    NUM_RECORDS = 1000000
    OUTPUT_FILE = "../locust/order_urls.txt"

    generate_order_urls(BASE_URL, NUM_RECORDS, OUTPUT_FILE)
    print(f"Все URL-адреса успешно записаны в {OUTPUT_FILE}")
