from app import schemas
from typing import List

# def test_get_all_posts(authorized_client, test_posts):
#     res = authorized_client.get("/posts/")
 
#     def validate(post):
#         return schemas.PostOut(**post)

#     posts_map = map(validate, res.json())
#     posts = list(posts_map)


#     assert  len(res.json()) == len(test_posts)
#     assert res.status_code == 200

# def test_unauthorized_user_get_all_posts(client, test_posts):
#     res = client.get("/posts/")
#     assert res.status_code == 401

# def test_unauthorized_user_get_one_post(client, test_posts):
#     res = client.get(f"/posts/{test_posts[0].id}")
#     assert res.status_code == 401

# def test_get_one_post_not_exist(authorized_client, test_posts):
#     res = authorized_client.get(f"/posts/88888")
#     assert res.status_code == 404

# def test_get_one_post(authorized_client, test_posts):
#     res = authorized_client.get(f"/posts/{test_posts[0].id}")
#     print(res.json()) 
#     post = schemas.Post(**res.json())

#     assert post.id == test_posts[0].id

# def test_unauthorized_user_delete_post(client, test_posts):
#     res = client.delete(f"/posts/{test_posts[0].id}")
#     assert res.status_code == 401

# def test_unauthorized_user_delete_post_success(authorized_client, test_posts):
#     res = authorized_client.delete(f"/posts/{test_posts[0].id}")

#     assert res.status_code == 204

# def test_delete_post_non_exist(authorized_client, test_posts):
#     res = authorized_client.delete(f"/posts/88888")
    
#     assert res.status_code == 404

# def test_delete_other_user_post(authorized_client, test_posts):
#     res = authorized_client.delete(f"/posts/{test_posts[3].id}")
#     print(test_posts[3].id)
#     print(res)
#     assert res.status_code == 403

def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated post",
        "content":"updated content",
        "id": test_posts[0].id
    }

    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data['title']

def test_update_other_user_post(authorized_client, test_user, test_user2, test_posts):
    data = {
            "title": "updated title",
            "content": "updated content",
            "id": test_posts[3].id
        }
    
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    print(res.json())
    assert res.status_code == 403