use 0525_new


DELIMITER //

CREATE PROCEDURE get_books_by_category(IN book_category VARCHAR(30))
BEGIN
    SELECT
        book_id,
        title,
        author,
        available_copies,
        total_copies
    FROM books
    WHERE category = book_category
    AND available_copies > 0;
END //

DELIMITER ;

-- 查詢程式設計類的書
CALL get_books_by_category('程式設計');

-- 查詢歷史類的書 
CALL get_books_by_category('歷史');



