# # from fastapi import APIRouter, HTTPException, status, Depends
# # from typing import List
# # from sqlmodel import Session, select
# # from sqlalchemy.orm import selectinload
# #
# # from ..models.posts import Post, PostCreate
# # from ..models.topics import Topic
# # from ..database import get_session
# #
# #
# # # Define the database engine (assuming the connection string is in get_db)
# # # engine = create_engine(get_session())
# #
# # router = APIRouter(prefix="/posts", tags=["posts"])
# #
# #
# # @router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
# # async def create_post(post_create: PostCreate, db: Session = Depends(get_session)):
# #     try:
# #
# #         post = Post(
# #             url=post_create.url,
# #             title=post_create.title,
# #             description=post_create.description,
# #             difficulty=post_create.difficulty,
# #             input_constraints=post_create.input_constraints,
# #             examples=post_create.examples,
# #         )
# #         for topic_id in post_create.topics:
# #             db_topic = db.get(Topic, topic_id)
# #             if db_topic:
# #                 post.topics.append(db_topic)
# #
# #         print("---> ")
# #         print("---> ", post)
# #         print("---> ")
# #
# #         db.add(post)
# #         db.commit()
# #         db.refresh(post)
# #         return post
# #     except Exception as e:
# #         raise HTTPException(
# #             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
# #             detail=f"Database error: {str(e)}",
# #         )
# #
# #
# # @router.get("/", response_model=List[Post])
# # async def get_all_posts(db: Session = Depends(get_session)):
# #     posts = db.exec(select(Post).options(selectinload(Post.topics)))
# #     return posts
# #
# #
# # @router.get("/{post_id}", response_model=Post)
# # async def get_post(post_id: int, db: Session = Depends(get_session)):
# #     post = db.get(Post, post_id)
# #     if not post:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
# #         )
# #     return post
# #
# #
# # @router.put("/{post_id}", response_model=Post)
# # async def update_post(post_id: int, post: Post, db: Session = Depends(get_session)):
# #     existing_post = db.get(Post, post_id)
# #     if not existing_post:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
# #         )
# #
# #     for field, value in post.model_dump().items():
# #         setattr(existing_post, field, value)
# #
# #     db.commit()
# #     db.refresh(existing_post)
# #     return existing_post
# #
# #
# # @router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
# # async def delete_post(post_id: int, db: Session = Depends(get_session)):
# #     post = db.get(Post, post_id)
# #     if not post:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
# #         )
# #
# #     db.delete(post)
# #     db.commit()
# #     return post

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List

# from ..database import get_db
# from ..schemas import posts as postSchema
# from ..models.posts import Post, InputConstraint, Example
# from ..models.topics import Topic

# router = APIRouter(prefix="/posts", tags=["posts"])


# @router.post("/", response_model=postSchema.Post, status_code=status.HTTP_201_CREATED)
# def create_post(post: postSchema.PostCreate, db: Session = Depends(get_db)):
#     db_post = Post(
#         url=post.url,
#         title=post.title,
#         description=post.description,
#         difficulty=post.difficulty,
#     )
#     if post.input_constraints:
#         db_post.input_constraints = [
#             InputConstraint(**ic.model_dump(), post=db_post)
#             for ic in post.input_constraints
#         ]
#     if post.examples:
#         db_post.examples = [
#             Example(**ex.model_dump(), post=db_post) for ex in post.examples
#         ]
#     if post.topics:
#         db_post.topics = db.query(Topic).filter(Topic.id.in_(post.topics)).all()
#     db.add(db_post)
#     db.commit()
#     db.refresh(db_post)
#     return db_post


# @router.get("/", response_model=List[postSchema.Post])
# def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return db.query(Post).offset(skip).limit(limit).all()


# @router.get("/{post_id}", response_model=postSchema.Post)
# def read_post(post_id: int, db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
#         )
#     return post


# @router.put("/{post_id}", response_model=postSchema.Post)
# def update_post(
#     post_id: int, post_update: postSchema.PostUpdate, db: Session = Depends(get_db)
# ):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if not db_post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
#         )
#     for key, value in post_update.dict(exclude_unset=True).items():
#         if key == "input_constraints":
#             db_post.input_constraints.clear()
#             if value:
#                 db_post.input_constraints.extend(
#                     [InputConstraint(**ic.dict(), post=db_post) for ic in value]
#                 )
#         elif key == "examples":
#             db_post.examples.clear()
#             if value:
#                 db_post.examples.extend(
#                     [Example(**ex.dict(), post=db_post) for ex in value]
#                 )
#         elif key == "topics":
#             db_post.topics = db.query(Topic).filter(Topic.id.in_(value)).all()
#         else:
#             setattr(db_post, key, value)
#     db.commit()
#     db.refresh(db_post)
#     return db_post


# @router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(post_id: int, db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if post:
#         db.delete(post)
#         db.commit()
#         return
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas.posts import PostCreate, PostUpdate, PostSchema
from ..models.posts import Post, InputConstraint, Example
from ..models.topics import Topic

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostSchema, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = Post(
        url=post.url,
        title=post.title,
        description=post.description,
        difficulty=post.difficulty,
    )
    if post.input_constraints:
        db_post.input_constraints = [
            InputConstraint(**ic.dict(), post=db_post) for ic in post.input_constraints
        ]
    if post.examples:
        db_post.examples = [Example(**ex.dict(), post=db_post) for ex in post.examples]
    if post.topics:
        db_post.topics = db.query(Topic).filter(Topic.id.in_(post.topics)).all()
    db.add(db_post)
    try:
        db.commit()
        db.refresh(db_post)
        return db_post
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating post: {e}")


@router.get("/", response_model=List[PostSchema])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Post).offset(skip).limit(limit).all()


@router.get("/{post_id}", response_model=PostSchema)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return post


@router.put("/{post_id}", response_model=PostSchema)
def update_post(post_id: int, post_update: PostUpdate, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    for key, value in post_update.dict(exclude_unset=True).items():
        if key == "input_constraints":
            db_post.input_constraints.clear()
            if value:
                db_post.input_constraints.extend(
                    [InputConstraint(**ic.dict(), post=db_post) for ic in value]
                )
        elif key == "examples":
            db_post.examples.clear()
            if value:
                db_post.examples.extend(
                    [Example(**ex.dict(), post=db_post) for ex in value]
                )
        elif key == "topics":
            db_post.topics = db.query(Topic).filter(Topic.id.in_(value)).all()
        else:
            setattr(db_post, key, value)
    try:
        db.commit()
        db.refresh(db_post)
        return db_post
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating post: {e}")


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        try:
            db.commit()
            return
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error deleting post: {e}")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
