import logging
import azure.functions as func
import mysql.connector
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Connect to MySQL
    cnx = mysql.connector.connect(
        user="<username>@<database_name>", 
        password='<password>', 
        host="<database_name>.mysql.database.azure.com", 
        port=3306
    )
    logging.info(cnx)
    # Delete all posts 
    cursor = cnx.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0; DELETE FROM `<database_name>`.posts WHERE `type` = 'post';")
    result_list = cursor.fetchall()
    # Build result response text
    result_str_list = []
    for row in result_list:
        row_str = ', '.join([str(v) for v in row])
        result_str_list.append(row_str)
    result_str = '\n'.join(result_str_list)
    return func.HttpResponse(
        result_str,
        status_code=200
    )
