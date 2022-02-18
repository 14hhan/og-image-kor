# og-image-kor
SNS에 웹 사이트의 링크를 공유할 때 보여지는 이미지를 동적으로 생성하는 프로젝트입니다.
![og image 만들기](https://og-image-kor.herokuapp.com/api/open-graph-image?title=OG%20image%20만들기&author=hywn)
![사이드 프로젝트 회고](https://og-image-kor.herokuapp.com/api/open-graph-image?title=사이드%20프로젝트%20회고&author=hywn.log&image_uri=https://user-images.githubusercontent.com/53527600/154746812-1e961716-4afb-4f55-9768-572a1a361907.jpg)

## Usage
```html
<meta property="og:image" content="https://og-image-kor.herokuapp.com/api/open-graph-image?title={title}&author={author}" />
```
또는
```html
<meta property="og:image" content="https://og-image-kor.herokuapp.com/api/open-graph-image?title={title}&author={author}&image_uri={image_uri}" />
```
- `title`(필수): 게시글의 제목
- `author`(필수): 작성자 또는 블로그 이름
- `image_uri`(optional): **1200*630** 크기의 이미지 주소
  - `image_uri`가 없을 경우 상단 첫번째로 보여지는 바다 이미지가 기본 배경이 됩니다.

## Upcoming Features
- [ ] title의 길이가 길 경우 자동 줄바꿈
- [ ] image_uri의 이미지 자동 크기 조정
- [ ] 기본 제공 배경 이미지 추가

추가되었으면 하는 기능이 있거나, 버그를 발견한 경우에는 `Issues` 또는 `Pull requests`를 이용해 알려 주세요!
