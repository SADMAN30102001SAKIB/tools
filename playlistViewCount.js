const videos = document.querySelectorAll('ytd-playlist-video-renderer');
const convertViews = (views) => {
  let num = parseFloat(views);
  if (views.includes("K")) {
    num *= 1000;
  } else if (views.includes("M")) {
    num *= 1000000;
  } else if (views.includes("B")) {
    num *= 1000000000;
  }
  return num;
}

let totalViews = 0
videos.forEach((vid) => {
    const views = vid.querySelector('#video-info > span:nth-child(1)')?.textContent.split(' ')[0] || '0'
    const converted = convertViews(views)
    totalViews += converted
})

console.log(totalViews)