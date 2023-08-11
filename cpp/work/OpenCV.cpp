#include "opencv2/core/matx.hpp"
#include "opencv2/imgcodecs.hpp"
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;
int main() {
    Mat src = imread("/Users/zhaolin/Downloads/src.png", IMREAD_UNCHANGED);
    Mat tex = imread("/Users/zhaolin/Documents/Projects/decorate_export_base/DecorateBusiness/cmake-build-release/panda/img/window.png", cv::IMREAD_UNCHANGED);

    cv::Point offset = {707, 636};
    cv::Point start = {434, 147}, end = {486, 147};
    // cv::Point start = {434, 147}, end = {343, 165};
    cv::Point2f p0 = start + offset, p1 = end + offset;
    int inDiff = 4, outDiff = 10;
    std::vector<cv::Point2f> tar_pts;
    // 计算斜线的向量
    cv::Point2f lineVector = p1 - p0;
    // 计算法线向量 顺时针转 90 度
    cv::Point2f dVector(lineVector.y, -lineVector.x);
    // 单位化法线向量
    cv::Point2f dNormVector = dVector / cv::norm(dVector);
    // 计算矩形的四个顶点 顺时针
    tar_pts.push_back(p1 - outDiff * dNormVector);
    tar_pts.push_back(p1 + inDiff * dNormVector);
    tar_pts.push_back(p0 + inDiff * dNormVector);
    tar_pts.push_back(p0 - outDiff * dNormVector);
    std::vector<cv::Point2f> tex_pts; // 左下角开始
    tex_pts.push_back(cv::Point2f(0, 0));
    tex_pts.push_back(cv::Point2f(0, tex.rows - 1));
    tex_pts.push_back(cv::Point2f(tex.cols - 1, tex.rows - 1));
    tex_pts.push_back(cv::Point2f(tex.cols - 1, 0));
    cv::Mat transMatrix = cv::getPerspectiveTransform(tex_pts, tar_pts);
    cv::Mat transTex;
    // 应用透视变换
    cv::warpPerspective(tex, transTex, transMatrix, src.size());
    // 混合图片
    cv::Mat result = cv::Mat::zeros(src.size(), src.type());
    for (int i = 0; i < src.rows; i++) {
        for (int j = 0; j < src.cols; j++) {
            // 获取transTex像素点的透明度
            float alpha = static_cast<float>(transTex.at<cv::Vec4b>(i, j)[3]) / 255.0;
            if (alpha) {
                result.at<cv::Vec4b>(i, j) = transTex.at<cv::Vec4b>(i, j);
            } else {
                result.at<cv::Vec4b>(i, j) = src.at<cv::Vec4b>(i, j);
            }
        }
    }
    // 显示结果
    cv::imshow("Tex", transTex);
    cv::imshow("Result", result);
    cv::waitKey(0);
    cv::destroyAllWindows();
    return 0;
}