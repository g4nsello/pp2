CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE ("PersonName" TEXT, "PhoneNumber" TEXT) AS $$
BEGIN
    RETURN QUERY 
    SELECT "PersonName", "PhoneNumber"
    FROM postgres.public.phone_book
    WHERE "PersonName" LIKE '%' || pattern || '%'
    OR "PhoneNumber" LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

