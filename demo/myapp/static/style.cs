/* BASE STYLING */

body {
  margin: 0;
  padding: 0;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, oxygen;
  background: #f4f5f7;
  color: #222;
}

.container {
  max-width: 800px;
  margin: 40px auto;
  padding: 0 20px;
}

h1, h2 {
  font-weight: 600;
  margin-bottom: 20px;
}

/* ADD ITEM BUTTON */
.add-btn {
  display: inline-block;
  margin-bottom: 20px;
  padding: 8px 14px;
  background: #0b5fff;
  color: white;
  border-radius: 6px;
  text-decoration: none;
  font-size: 15px;
}
.add-btn:hover {
  background: #004edb;
}

/* ITEM LIST */
.item-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
  padding: 0;
  list-style: none;
}

.item-card {
  background: white;
  padding: 15px 18px;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.item-card h3 {
  margin: 0 0 6px 0;
}

.item-meta {
  font-size: 13px;
  color: #6c6c6c;
  margin-top: 6px;
}

.item-actions {
  margin-top: 10px;
}

.item-actions a {
  margin-right: 12px;
  text-decoration: none;
  color: #0b5fff;
  font-weight: 500;
}

.item-actions a.delete {
  color: #d64545;
}

.item-actions a.delete:hover {
  color: #b33030;
}

/* FORMS */
form table td {
  padding: 6px 0;
}

button {
  padding: 8px 14px;
  background: #0b5fff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

button:hover {
  background: #004edb;
}

a.cancel-link {
  margin-left: 10px;
  text-decoration: none;
  color: #333;
}
