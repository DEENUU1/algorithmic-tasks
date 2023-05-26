SELECT DISTINCT v1.author_id AS id
FROM Views v1
JOIN Views v2 ON v1.author_id = v2.author_id AND v1.article_id = v2.article_id
WHERE v1.author_id = v1.viewer_id
ORDER BY id ASC;
