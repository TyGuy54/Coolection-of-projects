package database

import (
	"database/sql"
	"strconv"

	"blog-backend/model"

	_ "github.com/mattn/go-sqlite3"
)

// An important note: the sqlite3 driver returns a *DB.
// We’re storing it in the DB variable globally to use it without reconnecting.
// However, behind the scenes, the database/sql library maintains a connection pool
var DB *sql.DB

func ConnnectToDatabase() error {
	// creates a database connection to the sqlite database file
	db, err := sql.Open("sqlite3", "./sqlite/articals.sqlite3")
	if err != nil {
		return err
	}

	DB = db
	return nil
}

func GetArticals(count int) ([]model.Articals, error) {
	row, err := DB.Query("SELECT id, date, title, content from blog_articals LIMIT" + strconv.Itoa(count))
	if err != nil {
		// anytime sometines failes we return a nil for
		// the slice and an error
		return nil, err
	}
	// when this function completes this will be ran
	// clsoeng the connection
	defer row.Close()

	articals := make([]model.Articals, 0) // maing a new slice

	for row.Next() {
		singleArticals := model.Articals{}
		// scanning throgh all of the values returned
		// in the row and binding them to the singleArticals object
		err = row.Scan(
			&singleArticals.ID,
			&singleArticals.DATE,
			&singleArticals.TITLE,
			&singleArticals.CONTENT)

		if err != nil {
			// error checking for singleArticals
			return nil, err
		}

		// appending the singleArticals object to articals to be returned
		articals = append(articals, singleArticals)
	}

	err = row.Err()
	if err != nil {
		return nil, err
	}

	return articals, err
}

func GetArticalById(id string) (model.Articals, error) {
	stmt, err := DB.Prepare("SELECT id, date, title, content from blog_articals WHERE id = ?")

	if err != nil {
		return model.Articals{}, err
	}

	artical := model.Articals{}

	sqlErr := stmt.QueryRow(id).Scan(&artical.ID, &artical.DATE, &artical.TITLE, &artical.CONTENT)

	if err != nil {
		if sqlErr == sql.ErrNoRows {
			return model.Articals{}, err
		}
		return model.Articals{}, sqlErr
	}
	return artical, nil
}

func AddArticals(newArticals model.Articals) (bool, error) {
	tx, err := DB.Begin()

	if err != nil {
		return false, err
	}

	stmt, err := tx.Prepare("INSERT INTO blog_articals (date, title, content) VALUES (?,?,?)")

	if err != nil {
		return false, err
	}

	defer stmt.Close()

	_, err = stmt.Exec(newArticals.TITLE, newArticals.DATE, newArticals.CONTENT)

	if err != nil {
		return false, err
	}

	tx.Commit()

	return true, nil
}

func UpdateArticals(updatedArticals model.Articals, id int) (bool, error) {
	tx, err := DB.Begin()

	if err != nil {
		return false, err
	}

	stmt, err := tx.Prepare("UPDATE blog_articals SET date=?, title=?, content=? WHERE id=?")

	if err != nil {
		return false, err
	}

	defer stmt.Close() // closes the connection when the function is resolved

	_, err = stmt.Exec(updatedArticals.TITLE, updatedArticals.DATE, updatedArticals.CONTENT, updatedArticals.ID)

	if err != nil {
		return false, err
	}

	tx.Commit()

	return true, nil
}
